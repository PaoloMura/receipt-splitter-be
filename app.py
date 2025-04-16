from flask import Flask, request, jsonify 
import base64
import io 
from PIL import Image 
import pytesseract

app = Flask(__name__)

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

        extracted_text = pytesseract.image_to_string(image)

        return jsonify({
            "message": "Image received successfully!",
            "raw_text": extracted_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

