from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    from app.models import db
    db.init_app(app)
    
    # Import routes
    from app.routes import main
    app.register_blueprint(main)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Ensure upload directory exists
    upload_dir = os.path.join(app.instance_path, '..', app.config['UPLOAD_FOLDER'])
    os.makedirs(upload_dir, exist_ok=True)
    
    return app
