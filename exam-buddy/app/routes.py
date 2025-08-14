from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_from_directory, current_app
from app.models import db, Exam, Task, Note, Flashcard
from datetime import datetime, date
import os
from werkzeug.utils import secure_filename
import uuid

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@main.route('/')
def index():
    search = request.args.get('search', '')
    sort_by = request.args.get('sort', 'date')
    
    query = Exam.query
    
    if search:
        query = query.filter(
            (Exam.title.contains(search)) | 
            (Exam.subject.contains(search))
        )
    
    if sort_by == 'date':
        exams = query.order_by(Exam.date.asc()).all()
    elif sort_by == 'title':
        exams = query.order_by(Exam.title.asc()).all()
    else:
        exams = query.order_by(Exam.created_at.desc()).all()
    
    return render_template('index.html', exams=exams, search=search, sort_by=sort_by)

@main.route('/add_exam', methods=['GET', 'POST'])
def add_exam():
    if request.method == 'POST':
        try:
            subject = request.form['subject']
            # Generate title from subject and date
            exam_date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
            title = f"{subject} Exam - {exam_date.strftime('%B %d, %Y')}"
            
            exam_time = None
            if request.form.get('time'):
                exam_time = datetime.strptime(request.form['time'], '%H:%M').time()
            description = request.form.get('description', '')
            
            new_exam = Exam(
                title=title,
                subject=subject,
                date=exam_date,
                time=exam_time,
                description=description
            )
            
            db.session.add(new_exam)
            db.session.commit()
            
            flash('Exam added successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash('Error adding exam. Please try again.', 'error')
            
    return render_template('add_exam.html')

@main.route('/edit_exam/<int:exam_id>', methods=['GET', 'POST'])
def edit_exam(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    
    if request.method == 'POST':
        try:
            exam.title = request.form['title']
            exam.subject = request.form['subject']
            exam.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
            if request.form.get('time'):
                exam.time = datetime.strptime(request.form['time'], '%H:%M').time()
            else:
                exam.time = None
            exam.description = request.form.get('description', '')
            
            db.session.commit()
            flash('Exam updated successfully!', 'success')
            return redirect(url_for('main.exam_detail', exam_id=exam.id))
        except Exception as e:
            flash('Error updating exam. Please try again.', 'error')
    
    return render_template('edit_exam.html', exam=exam)

@main.route('/delete_exam/<int:exam_id>')
def delete_exam(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    try:
        # Delete associated files
        for note in exam.notes:
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], note.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
        
        db.session.delete(exam)
        db.session.commit()
        flash('Exam deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting exam. Please try again.', 'error')
    
    return redirect(url_for('main.index'))

@main.route('/exam/<int:exam_id>')
def exam_detail(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    return render_template('exam_detail.html', exam=exam)

@main.route('/add_task/<int:exam_id>', methods=['POST'])
def add_task(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    try:
        description = request.form['description']
        priority = request.form.get('priority', 'medium')
        
        new_task = Task(
            description=description,
            priority=priority,
            exam_id=exam_id
        )
        
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    except Exception as e:
        flash('Error adding task. Please try again.', 'error')
    
    return redirect(url_for('main.exam_detail', exam_id=exam_id))

@main.route('/toggle_task/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.exam_detail', exam_id=task.exam_id))

@main.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    exam_id = task.exam_id
    try:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting task. Please try again.', 'error')
    
    return redirect(url_for('main.exam_detail', exam_id=exam_id))

@main.route('/upload_note/<int:exam_id>', methods=['POST'])
def upload_note(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('main.exam_detail', exam_id=exam_id))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('main.exam_detail', exam_id=exam_id))
    
    if file and allowed_file(file.filename):
        try:
            original_filename = secure_filename(file.filename)
            # Generate unique filename to avoid conflicts
            filename = str(uuid.uuid4()) + '_' + original_filename
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Get file size
            file_size = os.path.getsize(file_path)
            
            new_note = Note(
                filename=filename,
                original_filename=original_filename,
                file_path=file_path,
                file_size=file_size,
                exam_id=exam_id
            )
            
            db.session.add(new_note)
            db.session.commit()
            flash('File uploaded successfully!', 'success')
        except Exception as e:
            flash('Error uploading file. Please try again.', 'error')
    else:
        flash('Invalid file type. Please upload a supported file format.', 'error')
    
    return redirect(url_for('main.exam_detail', exam_id=exam_id))

@main.route('/download_note/<int:note_id>')
def download_note(note_id):
    note = Note.query.get_or_404(note_id)
    upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
    return send_from_directory(
        upload_folder,
        note.filename,
        as_attachment=True,
        download_name=note.original_filename
    )

@main.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    exam_id = note.exam_id
    
    try:
        # Delete file from filesystem
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], note.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting note. Please try again.', 'error')
    
    return redirect(url_for('main.exam_detail', exam_id=exam_id))

@main.route('/countdown')
def countdown():
    exams = Exam.query.filter(Exam.date >= date.today()).order_by(Exam.date.asc()).all()
    return render_template('countdown.html', exams=exams)

@main.route('/api/exam_progress/<int:exam_id>')
def exam_progress(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    return jsonify({
        'progress': exam.progress_percentage(),
        'completed_tasks': sum(1 for task in exam.tasks if task.completed),
        'total_tasks': len(exam.tasks)
    })

# Flashcard routes
@main.route('/flashcards')
def flashcards():
    exams = Exam.query.all()
    return render_template('flashcards.html', exams=exams)

@main.route('/flashcards/<int:exam_id>')
def exam_flashcards(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    return render_template('exam_flashcards.html', exam=exam)

@main.route('/add_flashcard/<int:exam_id>', methods=['POST'])
def add_flashcard(exam_id):
    exam = Exam.query.filter_by(id=exam_id).first_or_404()
    try:
        topic = request.form['topic']
        summary = request.form['summary']
        
        new_flashcard = Flashcard(
            topic=topic,
            summary=summary,
            exam_id=exam_id
        )
        
        db.session.add(new_flashcard)
        db.session.commit()
        flash('Flashcard added successfully!', 'success')
    except Exception as e:
        flash('Error adding flashcard. Please try again.', 'error')
    
    return redirect(url_for('main.exam_flashcards', exam_id=exam_id))

@main.route('/delete_flashcard/<int:flashcard_id>')
def delete_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    exam_id = flashcard.exam_id
    try:
        db.session.delete(flashcard)
        db.session.commit()
        flash('Flashcard deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting flashcard. Please try again.', 'error')
    
    return redirect(url_for('main.exam_flashcards', exam_id=exam_id))
