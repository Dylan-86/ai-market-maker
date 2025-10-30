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

        # Initialize all fields to "Parsing failed"
        title = "Parsing failed: Title not found."
        underlying_metric = "Parsing failed: Underlying metric not found."
        url = "Parsing failed: URL not found."
        description = "Parsing failed: Description not found."
        score = "Parsing failed: Score not found."
        reason = "Parsing failed: Reason not found."

        # Regular expressions to extract data from the generated text
        title_match = re.search(r"<title>(.*?)</title>", generated_text, re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()

        metric_match = re.search(r"<underlying metric>(.*?)</underlying metric>", generated_text, re.DOTALL)
        if metric_match:
            underlying_metric = metric_match.group(1).strip()

        url_match = re.search(r"<url>(.*?)</url>", generated_text, re.DOTALL)
        if url_match:
            url = url_match.group(1).strip()

        description_match = re.search(r"<description>(.*?)</description>", generated_text, re.DOTALL)
        if description_match:
            description = description_match.group(1).strip()

        score_match = re.search(r"<score>(.*?)</score>", generated_text, re.DOTALL)
        if score_match:
            score = score_match.group(1).strip()

        reason_match = re.search(r"<reason>(.*?)</reason>", generated_text, re.DOTALL)
        if reason_match:
            reason = reason_match.group(1).strip()

        return jsonify({
            "generated_text": generated_text,
            "title": title,
            "underlying_metric": underlying_metric,
            "url": url,
            "description": description,
            "score": score,
            "reason": reason
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# SECURITY: remove the API key endpoint
# @app.route('/get_api_key', ...):  DELETE

if __name__ == "__main__":
    # Serve everything from this folder, including index.html and basic instructions.md
    app.run(host="127.0.0.1", port=5000, debug=True)
