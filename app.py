from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Thư mục lưu tệp upload
UPLOAD_FOLDER = '/var/www/storage/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Lưu file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "path": file_path}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1205)
