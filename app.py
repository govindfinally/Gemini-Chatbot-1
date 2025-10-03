# app.py
import os
import uuid
import logging
import time

# FLASK IMPORTS
from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler


from chatbot.chatbot_backend import generate_summary_and_keywords
from chatbot.text_to_speak import tts_generate_file
# --- END OF YOUR IMPORTS ---


# --- APP SETUP ---
app = Flask(__name__)
CORS(app)  # IMPROVEMENT: Enable Cross-Origin Resource Sharing for security

# --- CONFIGURATION ---
# IMPROVEMENT: Use app.config for better organization
app.config['AUDIO_FOLDER'] = os.path.join(app.root_path, "static", "audio")
app.config['AUDIO_FILE_LIFETIME_SECONDS'] = 3600  # Delete files after 1 hour

# Ensure the audio folder exists
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)


# --- BACKGROUND CLEANUP JOB ---
# IMPROVEMENT: This job automatically deletes old audio files to save server space.
def cleanup_old_audio_files():
    with app.app_context():
        folder = app.config['AUDIO_FOLDER']
        lifetime = app.config['AUDIO_FILE_LIFETIME_SECONDS']
        now = time.time()
        
        app.logger.info("Running scheduled cleanup of old audio files...")
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                file_age = now - os.path.getmtime(filepath)
                if file_age > lifetime:
                    try:
                        os.remove(filepath)
                        app.logger.info(f"Deleted old audio file: {filename}")
                    except OSError as e:
                        app.logger.error(f"Error deleting file {filename}: {e}")

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(cleanup_old_audio_files, 'interval', hours=1)
scheduler.start()


# --- ROUTES ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        if not data or not data.get("text", "").strip():
            return jsonify({"error": "No text provided"}), 400
        
        text = data["text"]
        
        # CORRECT: Calling your actual backend function from the import
        summary, keywords = generate_summary_and_keywords(text)
        
        return jsonify({"summary": summary, "keywords": keywords})

    except Exception as e:
        # IMPROVEMENT: Use Flask's logger and hide detailed errors in production
        app.logger.error(f"Summarize error: {e}")
        error_details = str(e) if app.debug else "An internal error occurred."
        return jsonify({"error": "Failed to generate summary", "details": error_details}), 500

@app.route("/speak", methods=["POST"])
def speak():
    try:
        data = request.get_json()
        if not data or not data.get("text", "").strip():
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]
        filename = f"tts_{uuid.uuid4().hex}.mp3"
        safe_filename = secure_filename(filename)
        filepath = os.path.join(app.config['AUDIO_FOLDER'], safe_filename)

        # CORRECT: Calling your actual text-to-speech function from the import
        tts_generate_file(text, filepath)
        
        # IMPROVEMENT: Provide URLs for both playing and downloading
        return jsonify({
            "audio_url": url_for("static", filename=f"audio/{safe_filename}"),
            "download_url": url_for("download_file", filename=safe_filename)
        })

    except Exception as e:
        app.logger.error(f"TTS generation error: {e}")
        error_details = str(e) if app.debug else "An internal error occurred."
        return jsonify({"error": "TTS generation failed", "details": error_details}), 500

@app.route("/download/<filename>")
def download_file(filename):
    safe_filename = secure_filename(filename)
    download_name = f"Govind_AI_Audio_{uuid.uuid4().hex[:6]}.mp3"
    return send_from_directory(
        app.config['AUDIO_FOLDER'], 
        safe_filename, 
        as_attachment=True,
        download_name=download_name
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True, host="0.0.0.0", port=5000)