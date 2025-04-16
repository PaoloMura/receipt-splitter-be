# 🧾 Receipt Splitter Backend

This is a simple Flask API that receives a base64-encoded image of a receipt and (eventually) processes it to extract items, so users can split the bill based on what they ordered.

## 🚀 Features

- Accepts a base64-encoded receipt image via a GET request
- Decodes and prepares the image for processing
- Placeholder for item extraction (OCR to be added)
- Returns JSON response (currently empty)

## 📦 Requirements

- Python 3.7+
- Flask
- Pillow

Install dependencies:

```bash
pip install -r requirements.txt
```


Setting Up:
# Virtual Environment:
Whenever starting a new project, you need to create a virtual environment for all your packages to be installed in:

```python3 -m venv env ```

*"env"* is the name of the environment
​
When the new environment has been created, you can tell by looking at the bottom left hand corner of visual studio code:

To activate the virtual environment, do the following command in the terminal:

```source env/bin/activate```

*"env/activate/bin"* is the directory of the activate script
