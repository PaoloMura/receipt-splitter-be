from google import genai
from dotenv import load_dotenv
import os
from PIL import Image
import json

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Use the API key in your application
print(f'Your API key is: {api_key}')

client = genai.Client(api_key=api_key)

prompt = "Extract the list of items and put it into a json with the following format: /{name:, quantity, price:,}."

image = Image.open("sampleImage2.jpg")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, prompt]
)

print("Raw Response:")
print(response.text)

print(type(response.text))
# Try parsing the response into a Python dict
parsed_json = json.loads(response.text)

# Save to a file
with open("response_output.json", "w") as f:
    json.dump(parsed_json, f, indent=2)

print("Saved response_output.json successfully.")