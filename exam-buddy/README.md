# Exam Buddy - Study Assistant Web Application

A minimalistic, interactive web application designed to help students manage their exam preparation efficiently. Built with Python Flask and SQLite, featuring a clean and responsive user interface.

## 🎯 Project Overview

Exam Buddy is a comprehensive study management system that helps students organize their exam schedules, track study progress, manage to-do lists, and store study materials. The application features a modern, minimalistic design with interactive elements to enhance the user experience.

## ✨ Features

### Core Functionality
- **📚 Exam Management**: Add, edit, delete, and view exam details (title, subject, date, time, description)
- **🔍 Search & Sort**: Search exams by title/subject and sort by date, title, or creation date
- **⏰ Countdown Dashboard**: Live countdown timers showing days remaining until exams
- **✅ To-Do Lists**: Create and manage study tasks for each exam with priority levels
- **📈 Progress Tracking**: Visual progress bars showing completion percentage
- **📄 File Upload**: Upload and manage study notes/PDFs for each exam
- **🔔 Study Reminders**: Browser notification reminders to encourage regular study
- **💬 Motivational Quotes**: Rotating inspirational quotes to keep students motivated

### Technical Features
- **🗄️ SQLite Database**: Persistent data storage for exams, tasks, and notes
- **📱 Responsive Design**: Mobile-friendly interface that works on all devices
- **🎨 Modern UI**: Clean, minimalistic design with Font Awesome icons
- **⚡ Interactive Elements**: Animated progress bars and smooth transitions
- **📁 File Management**: Secure file upload and download system
- **🔒 Data Validation**: Form validation and error handling

## 🛠️ Technologies Used

### Backend
- **Python 3.7+**
- **Flask 2.3.3** - Web framework
- **Flask-SQLAlchemy 3.0.5** - Database ORM
- **SQLite** - Database engine
- **Werkzeug 2.3.7** - WSGI utilities

### Frontend
- **HTML5** - Structure and markup
- **CSS3** - Styling with flexbox/grid and animations
- **JavaScript (ES6)** - Interactive functionality
- **Font Awesome 6.0** - Icons and visual elements

## 📁 Project Structure

```
exam-buddy/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── routes.py                # Application routes and logic
│   ├── models.py                # Database models (Exam, Task, Note)
│   ├── templates/               # HTML templates
│   │   ├── base.html           # Base template with navigation
│   │   ├── index.html          # Dashboard/home page
│   │   ├── add_exam.html       # Add new exam form
│   │   ├── edit_exam.html      # Edit exam form
│   │   ├── exam_detail.html    # Exam details with tasks/notes
│   │   └── countdown.html      # Countdown page
│   └── static/                 # Static assets
│       ├── css/
│       │   └── style.css       # Main stylesheet
│       ├── js/
│       │   ├── main.js         # Main JavaScript functionality
│       │   └── quotes.js       # Motivational quotes system
│       └── uploads/            # Uploaded files storage
├── config.py                   # Application configuration
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project
Navigate to your desired directory and ensure you have the project files in:
```
C:\Users\Admin\OneDrive\Desktop\WT project\project 2\exam-buddy\
```

### Step 2: Create Virtual Environment (Recommended)
```bash
cd "C:\Users\Admin\OneDrive\Desktop\WT project\project 2\exam-buddy"
python -m venv venv
```

### Step 3: Activate Virtual Environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
python run.py
```

### Step 6: Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## 💻 How to Use

### Getting Started
1. **Add Your First Exam**: Click "Add New Exam" to create your first exam entry
2. **Fill in Details**: Enter exam title, subject, date, optional time, and description
3. **Manage Tasks**: Navigate to exam details to add study tasks with priority levels
4. **Upload Notes**: Add study materials by uploading files (PDF, DOC, images, etc.)
5. **Track Progress**: Watch your progress bar fill as you complete tasks

### Main Features Usage

#### Dashboard
- View all your exams in a card-based layout
- See progress bars, task counts, and days remaining
- Use search to find specific exams
- Sort exams by date, title, or creation time

#### Exam Management
- **Add Exam**: Use the "Add New Exam" button or navigation link
- **Edit Exam**: Click the edit (pencil) icon on any exam card
- **Delete Exam**: Click the delete (trash) icon with confirmation prompt
- **View Details**: Click the view (eye) icon to see full exam details

#### Task Management
- Add tasks with low/medium/high priority levels
- Check off completed tasks to update progress
- Delete tasks that are no longer relevant

#### File Management
- Upload study notes in supported formats (PDF, DOC, images, TXT)
- Download uploaded files at any time
- Delete files when no longer needed

#### Countdown Timer
- Visit the "Countdown" page to see time remaining for upcoming exams
- Automatic calculation of days remaining
- Visual indicators for today's exams and overdue items

### Tips for Best Experience
- Enable browser notifications for study reminders
- Keep task descriptions clear and specific
- Upload organized study materials for easy access
- Check the dashboard regularly to stay on track

## 🔧 Configuration

### Database Configuration
The app uses SQLite by default. To use a different database, modify `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'your-database-url-here'
```

### File Upload Configuration
Supported file formats can be modified in `config.py`:
```python
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
```

### Security Configuration
For production deployment, change the secret key in `config.py`:
```python
SECRET_KEY = 'your-production-secret-key'
```

## 🐛 Troubleshooting

### Common Issues

**Port already in use:**
- Change the port in `run.py`: `app.run(debug=True, port=5001)`

**Database errors:**
- Delete `exam_buddy.db` file and restart the app to recreate the database

**File upload not working:**
- Check that the `uploads` directory exists and has write permissions

**Styles not loading:**
- Ensure Flask is serving static files correctly
- Check browser developer tools for 404 errors

### Getting Help
If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure you're running the correct Python version
4. Check file permissions for the project directory

## 🔮 Future Enhancements

Potential features for future versions:
- User authentication and multi-user support
- Email/SMS reminder notifications
- Study schedule generator
- Performance analytics and insights
- Integration with calendar applications
- Mobile app version
- Cloud synchronization
- Collaborative study groups

## 📄 License

This project is created for educational purposes. Feel free to modify and distribute as needed.

## 🤝 Contributing

This project is designed as a learning exercise. Suggestions and improvements are welcome!

---

**Happy Studying! 📚✨**
