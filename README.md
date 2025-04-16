# 🧾 Receipt Splitter API

This is a simple Flask API that receives a base64-encoded image of a receipt and using Google Gemini it processes and extracts the items and prices from the image into a list, so users can split the bill based on what they ordered. The list is return as a simple JSON object.

## 🚀 Features

- Accepts a base64-encoded receipt image via a GET request
- Decodes and prepares the image for processing
- Returns JSON response

## 📦 Requirements

- Python 3.7+
- Flask
- Pillow
- Google-genai
- Pytesseract

Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Setup

1. Clone the repo 
2. Create .env containing Google Gemini API key
3. Create Virtual Environment if necessary
4. Install all dependencies


# Virtual Environment:
1. Whenever starting a new project, you need to create a virtual environment for all your packages to be installed in:

```python3 -m venv env ```

*"env"* is the name of the environment

2. To activate the virtual environment, do the following command in the terminal:

```source env/bin/activate```

*"env/activate/bin"* is the directory of the activate script

3. Install dependencies 

```pip install -r requirements.txt ```

4. Run Flask server:

```python app.py```
