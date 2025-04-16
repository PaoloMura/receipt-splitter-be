from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

# Load the environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv('API_KEY')

# Use the API key in your application
print(f'Your API key is: {api_key}')

client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=["How does AI work?"]
# )
# print(response.text)

prompt = "Extract the list of items and put it into a json with the following format: /{name:, quantity, price:,}."

image = Image.open("sampleImage2.jpg")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, prompt]
)
print(response.text)