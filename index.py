import requests
import base64
import json
import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai


# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Use the API key in your application
print(f'Your API key is: {api_key}')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, welcome to the homepage!'

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    try:
        # Get image and prompt from the request
        image_file = request.files.get('image')
        prompt_text = request.form.get('prompt', 'Get the list of items in a json format like this: /{description:,price}')
        
        # Check if image was provided
        if not image_file:
            return jsonify({'error': 'No image provided'}), 400
        
        # Read and encode the image
        image_data = image_file.read()
        
        # Configure the model
        model = genai.GenerativeModel('gemini-2.0-pro-vision')
        
        # Create the request
        response = model.generate_content(
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": prompt_text},
                        {"inline_data": {
                            "mime_type": image_file.content_type,
                            "data": base64.b64encode(image_data).decode('utf-8')
                        }}
                    ]
                }
            ],
            generation_config={
                "response_mime_type": "application/json"
            }
        )
        
        # Return the response as JSON
        return jsonify(response.text)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)