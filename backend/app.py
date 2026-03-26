from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'resumes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "TrueHire Backend Running"

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"message": "Resume uploaded", "filename": file.filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
