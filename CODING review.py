from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_file.db'  # Update this with your database URI

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

# Define your SQLAlchemy models here
class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add your model fields here

# Create the tables in the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
