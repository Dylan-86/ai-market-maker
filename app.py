# /home/ddy/Apps/dexetera/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from google import genai
import re

load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)
model = client.models


@app.route('/generate_market', methods=['POST'])
def generate_market():
    user_input = request.json['user_input']

    # Read instructions from the file
    with open('basic instructions.md', 'r') as f:
        instructions = f.read()

    prompt = f"{instructions}\nUser Idea: {user_input}\n\nOutput:"

    try:
        response = model.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        generated_text = response.text

        description = "Parsing failed: Description not found."
        url = "Parsing failed: URL not found."

        # Find the summary line which contains all the market data
        summary_line = ""
        for line in generated_text.split('\n'):
            if "Market title:" in line and "Market description:" in line:
                summary_line = line.strip().replace('`', '')  # Clean backticks
                break
        
        if summary_line:
            # Regex to extract the description between "Market description:" and the next key.
            desc_match = re.search(r'Market description:(.*?)(Underlying metric \(URL\):|Interest rating:)', summary_line)
            if desc_match:
                description = desc_match.group(1).strip()

            # Regex to find the first full URL in the summary line.
            url_match = re.search(r'https?://[^\s]+', summary_line)
            if url_match:
                url = url_match.group(0)


        return jsonify({
            'generated_text': generated_text,
            'description': description,
            'url': url
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_api_key', methods=['GET'])
def get_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return jsonify({'error': 'GEMINI_API_KEY not found'}), 500
    return jsonify({'api_key': api_key})

if __name__ == '__main__':
    app.run(debug=True)