import base64
import io
import json
import os
import re
from PIL import Image
import pytesseract
from google import genai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Initialize the Google Gemini client
client = genai.Client(api_key=api_key)

# Decode base64 string to PIL image
def decode_image(base64_string):
    if base64_string.startswith("data:image"):
        base64_string = base64_string.split(",")[1]
    image_bytes = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(image_bytes))


# OCR with Tesseract and custom parsing
def extract_items_using_tesseract(image):
    raw_text = pytesseract.image_to_string(image)
    lines = raw_text.splitlines()
    items = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Detect '2x Burger $6.00' or 'Coke x3 $5.25' formats
        match = re.search(r'(?:(\d+)[xX]\s*)?(.*?)(?:[xX](\d+)\s*)?\$?(\d+\.\d{2})$', line)
        if match:
            qty1 = match.group(1)  # First quantity part (e.g., 2 in '2x Burger')
            name = match.group(2).strip()  # Item name (e.g., 'Burger')
            qty2 = match.group(3)  # Second quantity part (e.g., 3 in 'Coke x3')
            total_price = float(match.group(4))  # Total price (e.g., 6.00)

            # Determine the quantity based on xN or Nx pattern
            quantity = int(qty1 or qty2 or 1)  # Default to 1 if no quantity is found
            unit_price = round(total_price / quantity, 2)  # Calculate price per unit

            # Skip lines like 'total', 'tax', 'subtotal', etc.
            if name.lower() in ['total', 'tax', 'subtotal']:
                continue

            # Add the item multiple times based on the quantity
            for _ in range(quantity):
                items.append({
                    "name": name,
                    "price": unit_price
                })
    return {
        "raw_text": raw_text,
        "items": items
    }
