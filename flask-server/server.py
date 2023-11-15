# app.py

import subprocess
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from urllib.parse import quote


app = Flask(__name__)
CORS(app, supports_credentials=True)
# Replace special characters in the password
password = '1120'
quoted_password = quote(password)

# Use the quoted password in the URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{quoted_password}@129.232.253.178/lms'
app.config['SQLALCHEMY_PORT'] = 3306
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class EmotionData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30), nullable=False)
    face_id = db.Column(db.Integer, nullable=False)
    emotion_label = db.Column(db.String(20), nullable=False)
    emotion_score = db.Column(db.Float, nullable=False)
    average_score = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(50), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/start-desktop-app', methods=['POST'])
def start_desktop_app():
    try:

        # Add code here to start your desktop application.
        # Replace 'your_desktop_app_command' with the actual command to start your desktop app.
        # For example, if your desktop app is a Python script, you can use 'python your_app.py'.
        # Ensure that the command is appropriate for starting your specific desktop application.
        # Example: Starting a Python script
        # Replace 'your_app.py' with the actual filename of your Python script.
        subprocess.Popen(['python',
                          r'C:\Users\Proline\Downloads\Emotion_detect - Copy\Emotion_detect - Copy\TestEmotionDetector.py'],
                         shell=True)



        response = {'message': 'Desktop app started successfully'}
        return jsonify(response), 200
    except Exception as e:
        response = {'message': f'Error starting the desktop app: {str(e)}'}
        return jsonify(response), 500


if __name__ == '__main__':
    app.run(debug=True)
