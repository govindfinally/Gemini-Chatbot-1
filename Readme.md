# 🚀 Govind's AI Suite - Text Summarizer & TTS

A beautiful, modern web application that provides AI-powered text summarization and text-to-speech conversion with a stunning dark-themed UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📊 AI Text Summarization**: Automatically generate concise summaries from long texts
- **🏷️ Keyword Extraction**: Identify and extract key topics and important keywords
- **🔊 Text-to-Speech**: Convert any text into natural-sounding audio
- **🎨 Modern UI**: Beautiful dark theme with glassmorphism effects and smooth animations
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **⚡ Real-time Processing**: Fast API responses with loading indicators
- **🎵 Audio Playback**: Built-in audio player with download capabilities

## 🖼️ Screenshots

### Main Interface
The application features a stunning dark UI with animated gradients, twinkling stars, and smooth transitions.

### Tab-Based Navigation
- **Summarizer Tab**: Input text and get AI-generated summaries with keyword tags
- **Text-to-Speech Tab**: Convert text to audio with instant playback

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI/ML**: Custom summarization and TTS engines
- **Styling**: Custom CSS with glassmorphism and modern animations
- **Typography**: Google Fonts (Inter)

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Flask
- Required Python libraries (see Installation)

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/govindfinally/Gemini-Chatbot-1.git
cd Gemini-Chatbot-1
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install flask werkzeug
```

4. **Install additional required packages**
```bash
# Add your specific dependencies for chatbot backend and TTS
pip install -r requirements.txt
```

## 📁 Project Structure

```
Gemini-Chatbot-1/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── chatbot/
│   ├── __init__.py
│   ├── chatbot_backend.py         # Summarization & keyword extraction
│   └── text_to_speak.py           # Text-to-speech generation
│
├── templates/
│   └── index.html                 # Main UI template
│
└── static/
    └── audio/                     # Generated TTS audio files
```

## 🎯 Usage

1. **Start the Flask server**
```bash
python app.py
```

2. **Open your browser**
Navigate to:
```
http://localhost:5000
```
Or access from other devices on your network:
```
http://your-ip-address:5000
```

3. **Use the application**

   **For Summarization:**
   - Click on the "Text Summarizer" tab
   - Paste or type your text in the input area
   - Click "Generate Summary"
   - View the AI-generated summary and extracted keywords

   **For Text-to-Speech:**
   - Click on the "Text-to-Speech" tab
   - Enter the text you want to convert
   - Click "Generate Audio"
   - Listen to the generated audio or download it

## 🔧 Configuration

### Audio Storage
Audio files are stored in `static/audio/` directory. The application automatically creates this folder if it doesn't exist.

### Port Configuration

The application runs on **port 5000** by default and is accessible on all network interfaces (`0.0.0.0`).

**Development** (current setup):
```python
app.run(debug=True, host="0.0.0.0", port=5000)
```

This means:
- **Local access**: `http://localhost:5000`
- **Network access**: `http://YOUR_IP:5000` (accessible from other devices on your network)

**To change the port**, modify the last line in `app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=8080)  # Example: port 8080
```

**Production** (recommended):
Use a production-ready WSGI server like Gunicorn or uWSGI:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📡 API Endpoints

### POST `/summarize`
Generate summary and extract keywords from text.

**Request Body:**
```json
{
  "text": "Your long text here..."
}
```

**Response:**
```json
{
  "summary": "Generated summary...",
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

### POST `/speak`
Convert text to speech and return audio URL.

**Request Body:**
```json
{
  "text": "Text to convert to speech..."
}
```

**Response:**
```json
{
  "audio_url": "/static/audio/tts_abc123.mp3"
}
```

### GET `/download/<filename>`
Download generated audio files.

## 🎨 Customization

### Changing Colors
Edit the CSS gradient values in `templates/index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Modifying Animations
Adjust animation timing and effects in the `@keyframes` sections of the CSS.

### Adding Features
Extend the Flask routes in `app.py` and update the frontend JavaScript accordingly.

## 🐛 Troubleshooting

### Audio files not playing
- Ensure the `static/audio/` directory exists and has write permissions
- Check browser console for CORS or file path issues

### Summarization not working
- Verify `chatbot_backend.py` is properly configured
- Check if all required NLP libraries are installed

### Port already in use
Change the port in `app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=8000)  # Use different port
```

## 🔐 Security Considerations

- **File Upload Validation**: Uses `secure_filename()` to prevent directory traversal
- **Input Sanitization**: Always validate and sanitize user inputs
- **Production Deployment**: Never use `debug=True` in production
- **HTTPS**: Use HTTPS in production to encrypt data transmission

## 🚀 Deployment

### Deploy to Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create gemini-chatbot-1
git push heroku main
```

### Deploy to AWS/Azure/GCP
Follow platform-specific deployment guides for Flask applications.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Govind**

- Built with ❤️ using Flask and modern web technologies
- For questions or suggestions, feel free to reach out!

## 🙏 Acknowledgments

- Flask framework and community
- Contributors to the NLP and TTS libraries used
- Inspiration from modern web design trends

## 📈 Future Enhancements

- [ ] Multi-language support for summarization and TTS
- [ ] User authentication and history tracking
- [ ] Batch processing for multiple texts
- [ ] PDF and document upload support
- [ ] Custom voice selection for TTS
- [ ] API rate limiting and caching
- [ ] Real-time collaboration features
- [ ] Export summaries to various formats (PDF, DOCX)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

⭐ If you found this project helpful, please consider giving it a star!

**Made with passion by Govind** 🚀