from flask import Flask, render_template, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
import os
import uuid
from chatbot.chatbot_backend import generate_summary_and_keywords
from chatbot.text_to_speak import tts_generate_file

app = Flask(__name__)

# Ensure audio folder exists
AUDIO_FOLDER = os.path.join(app.root_path, "static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json or request.form
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        summary, keywords = generate_summary_and_keywords(text)
        return jsonify({"summary": summary, "keywords": keywords})
    except Exception as e:
        return jsonify({"error": "Backend error", "details": str(e)}), 500


@app.route("/speak", methods=["POST"])
def speak():
    data = request.json or request.form
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # generate unique filename
    uid = uuid.uuid4().hex
    filename = secure_filename(f"tts_{uid}.mp3")
    filepath = os.path.join(AUDIO_FOLDER, filename)

    try:
        # Save TTS file
        tts_generate_file(text, filepath)
        file_url = url_for("static", filename=f"audio/{filename}")
        return jsonify({"audio_url": file_url})
    except Exception as e:
        return jsonify({"error": "TTS generation failed", "details": str(e)}), 500


@app.route("/download/<filename>")
def download_file(filename):
    filepath = os.path.join(AUDIO_FOLDER, secure_filename(filename))
    if not os.path.exists(filepath):
        return "File not found", 404
    return send_file(filepath, as_attachment=True)


if __name__ == "__main__":
    # for dev use only; in production use gunicorn/uwsgi
    app.run(debug=True, host="0.0.0.0", port=5000)
