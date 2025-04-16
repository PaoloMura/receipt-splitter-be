from flask import Flask, request, jsonify 
import base64
import io 
from PIL import Image 

app = Flask(__name__)

@app.route('/upload-receipt', methods=['POST'])
def upload_receipt():
    data = request.get_json()
    image_b64 = data.get('image')

    # Optional: Strip the prefix if it's there
    if image_b64.startswith("data:image"):
        image_b64 = image_b64.split(",")[1]

    try:
        # Decode base64 to image
        image_bytes = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes))

        # Now you can run OCR on `image`
        # Example:
        # import pytesseract
        # text = pytesseract.image_to_string(image)

        return jsonify({"message": "Image received successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

