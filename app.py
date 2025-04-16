from flask import Flask, request, jsonify 
import base64
import io 
from PIL import Image 
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image
import json
import re

app = Flask(__name__)

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

client = genai.Client(api_key=api_key)

prompt = "Extract the list of items and put it into a json with the following format: /{name:, quantity, price:,}."

@app.route('/upload-receipt', methods=['POST'])
def upload_receipt():
    data = request.get_json()
    image_b64 = data.get('image')

    if not image_b64:
        return jsonify({"error": "No image provided"}), 400

    # Optional: Strip the prefix if it's there
    if image_b64.startswith("data:image"):
        image_b64 = image_b64.split(",")[1]

    try:
        # Decode base64 to image
        image_bytes = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes))

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[image, prompt]
        )       

        raw_text = response.text.strip()

        # Remove markdown-style ```json ... ```
        if raw_text.startswith("```json"):
            raw_text = re.sub(r"^```json\s*|\s*```$", "", raw_text.strip())

        # Parse the JSON string into a Python object
        try:
            parsed_json = json.loads(raw_text)
        except json.JSONDecodeError as e:
            print("JSON parsing failed:", e)
            with open("raw_failed_output.txt", "w") as f:
                f.write(raw_text)
            return jsonify({"error": "JSON parsing failed"}), 400
        print(parsed_json)
        print(type(parsed_json))
        return jsonify(parsed_json), 200

        # return jsonify({
        #     "message": "Image received successfully!",
        #     "extracted_data": parsed_json}), 200

    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

