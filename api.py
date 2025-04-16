from google import genai
from dotenv import load_dotenv
import os
from PIL import Image
import json
import re

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

client = genai.Client(api_key=api_key)

prompt = "Extract the list of items and put it into a json with the following format: /{label:, quantity, cost:,}."

image = Image.open("sampleImage2.jpg")
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
    exit(1)

# Print the parsed_json as a JSON string
json_data = json.dumps(parsed_json, indent=2, ensure_ascii=False)
print(json_data)

print("Saved response_output.json successfully.")