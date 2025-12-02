from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='/')
CORS(app)

# Serve homepage
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Contact form endpoint
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json() or {}
    name = data.get('name', 'Anonymous')
    email = data.get('email', '')
    message = data.get('message', '')

    # Simple server-side logging — edit to save to file or send email
    print("=== Contact form submission ===")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)
    print("===============================")

    # Return a JSON response to the frontend
    return jsonify({"message": "Thanks! Your message was received."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
