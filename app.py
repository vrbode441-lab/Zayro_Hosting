from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Hosting Platform!"

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # logic to save the file and return response
    return jsonify({'message': 'File uploaded successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)