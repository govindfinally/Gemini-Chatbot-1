import pyttsx3
from chatbot.chatbot_backend import generate_summary_and_keywords
from gtts import gTTS


class TextToSpeak:
    def __init__(self, input_text: str):
        # Generate summary + keywords
        summary_text, keywords_text = generate_summary_and_keywords(input_text)

        # Save them as instance variables
        self.summary_text = summary_text or "No summary generated."
        self.keywords_text = keywords_text or "No keywords generated."

        # Initialize speech engine
        self.engine = pyttsx3.init()

    def speak(self):
        # Speak summary and keywords in one run
        self.engine.say("Here is the summary.")
        self.engine.say(self.summary_text)

        self.engine.say("And here are the keywords.")
        self.engine.say(self.keywords_text)

        self.engine.runAndWait()


def tts_generate_file(text: str, filepath: str):
    """
    Generate an MP3 file for the given text using gTTS.
    This is used in the Flask app to save audio files.
    """
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filepath)
    except Exception as e:
        raise RuntimeError(f"TTS generation failed: {e}")
