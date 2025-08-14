from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='exam', lazy=True, cascade='all, delete-orphan')
    notes = db.relationship('Note', backref='exam', lazy=True, cascade='all, delete-orphan')
    flashcards = db.relationship('Flashcard', backref='exam', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Exam {self.title}>'

    def progress_percentage(self):
        """Calculate completion percentage of tasks for this exam"""
        if not self.tasks:
            return 0
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        return int((completed_tasks / len(self.tasks)) * 100)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), default='medium')  # low, medium, high
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.description}>'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=True)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)

    def __repr__(self):
        return f'<Note {self.original_filename}>'

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)

    def __repr__(self):
        return f'<Flashcard {self.topic}>'
