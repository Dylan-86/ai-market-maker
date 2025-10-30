# app.py
# /home/ddy/Apps/dexetera/app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from google import genai
import re

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTR_PATH = os.path.join(BASE_DIR, "basic instructions.md")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found in .env file")

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")
CORS(app, resources={r"/generate_market": {"origins": "*"}})  # keep narrow if you want

client = genai.Client(api_key=GEMINI_API_KEY)

@app.route("/")
def root():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/generate_market", methods=["POST"])
def generate_market():
    data = request.get_json(silent=True) or {}
    user_input = (data.get("user_input") or "").strip()
    if not user_input:
        return jsonify({"error": "user_input is required"}), 400

    try:
        with open(INSTR_PATH, "r", encoding="utf-8") as f:
            instructions = f.read()
    except FileNotFoundError:
        return jsonify({"error": f"Instructions file not found at {INSTR_PATH}"}), 500

    prompt = f"{instructions}\nUser Idea: {user_input}\n\nOutput:"

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
        generated_text = resp.text or ""

        description = "Parsing failed: Description not found."
        url = "Parsing failed: URL not found."

        summary_line = ""
        for line in generated_text.splitlines():
            if "Market title:" in line and "Market description:" in line:
                summary_line = line.strip().replace("`", "")
                break

        if summary_line:
            m = re.search(
                r"Market description:(.*?)(Underlying metric \(URL\):|Interest rating:)",
                summary_line
            )
            if m:
                description = m.group(1).strip()
            m2 = re.search(r"https?://[^\s]+", summary_line)
            if m2:
                url = m2.group(0)

        return jsonify({
            "generated_text": generated_text,
            "description": description,
            "url": url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# SECURITY: remove the API key endpoint
# @app.route('/get_api_key', ...):  DELETE

if __name__ == "__main__":
    # Serve everything from this folder, including index.html and basic instructions.md
    app.run(host="127.0.0.1", port=5000, debug=True)
