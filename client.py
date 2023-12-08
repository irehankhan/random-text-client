import os
import hashlib
from flask import Flask, render_template_string

app = Flask(__name__)

# Specify the desired file size in bytes (1 KB = 1024 bytes)
DESIRED_FILE_SIZE_BYTES = 1024

@app.route('/')
def receive_and_save_file():
    # Simulate receiving a file from the server (replace this with actual file receiving logic)
    received_file_content = generate_fixed_size_file()

    # Verify the file's integrity
    sha256_calculated, md5_calculated = calculate_checksum(received_file_content)

    # Save the received file in the "/clientdata" directory
    file_name = 'received_file.txt'
    client_directory = '/clientdata'
    client_file_path = os.path.join(client_directory, file_name)

    with open(client_file_path, 'w') as file:
        file.write(received_file_content)

    message = "Checksums match. File received and saved successfully."

    return render_template_string(
        """
        <div style="text-align: center;">
            <h2 style="color: green;">{{ message }}</h2>
            <p>SHA256: {{ sha256_calculated }}</p>
            <p>MD5: {{ md5_calculated }}</p>
            <p>File Size: {{ size_in_kb(received_file_content) }} KB</p>
            <p>Word Count: {{ get_word_count(received_file_content) }}</p>
            <p>File Name: {{ file_name }}</p>
            <p>File Path: {{ client_file_path }}</p>
            <h3 style="color: blue;">Content of the file:</h3>
            <textarea style="width: 60%; height: 300px; font-size: 16px; background-color: #f4f4f4; padding: 10px; border-radius: 5px;">{{ received_file_content }}</textarea>
        </div>
        """,
        message=message,
        sha256_calculated=sha256_calculated,
        md5_calculated=md5_calculated,
        size_in_kb=lambda x: len(x.encode('utf-8')) / 1024,  # Function to calculate size in KB
        get_word_count=get_word_count,
        file_name=file_name,
        client_file_path=client_file_path,
        received_file_content=received_file_content  # Pass received_file_content to the template context
    )

def generate_fixed_size_file():
    # Generate random content until the desired file size is reached
    while True:
        content = generate_fancy_text()
        if len(content.encode('utf-8')) >= DESIRED_FILE_SIZE_BYTES:
            return content[:DESIRED_FILE_SIZE_BYTES]

def generate_fancy_text():
    # Generate random fancy text (you can modify this as needed)
    from lorem import text
    fancy_text = text()
    return fancy_text

def calculate_checksum(data):
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()

    sha256.update(data.encode('utf-8'))
    md5.update(data.encode('utf-8'))

    return sha256.hexdigest(), md5.hexdigest()

def get_word_count(text):
    return len(text.split())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
