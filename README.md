# 🎤 Hindi Audio → English Translator

An AI-powered Streamlit application that transcribes **Hindi audio into text** and translates it into **English** using **OpenAI Whisper**.

---

## 📌 Overview

The Hindi Audio → English Translator is a speech-processing application that enables users to upload Hindi audio files and instantly obtain:

* 📝 Hindi Transcription
* 🌍 English Translation

The application leverages **OpenAI Whisper Large-v3** for highly accurate multilingual speech recognition and translation.

---

## ✨ Features

* Upload audio files in multiple formats.
* Automatic Hindi speech transcription.
* Instant English translation.
* Long audio support through chunk-based processing.
* Audio validation and preprocessing.
* User-friendly Streamlit interface.
* Download sample audio files.
* Session state management for improved performance.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI/ML

* OpenAI Whisper

### Audio Processing

* PyDub
* NumPy
* FFmpeg

### Utilities

* Tempfile
* Hashlib
* OS

---

## 📂 Project Structure

```text
AUDIO_TRANSLATOR/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   ├── Logo_TechOptima_update.png
│   └── techoptima-01.jpg
│
├── sample_files/
│   └── sample_audio_files.zip
│
├── audio_translator/
│   ├── __init__.py
│   ├── config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── whisper_model.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── transcription_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── audio_utils.py
│   │   ├── file_utils.py
│   │   └── session_utils.py
│   │
│   └── ui/
│       ├── __init__.py
│       ├── sidebar.py
│       ├── upload_section.py
│       └── about_section.py
│
└── temp/
```

---

# 🚀 Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/audio-translator.git

cd audio-translator
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Whisper Setup

This project uses **OpenAI Whisper** for speech recognition and translation.

## Install Whisper

```bash
pip install openai-whisper
```

Alternatively:

```bash
pip install git+https://github.com/openai/whisper.git
```

---

# 🔥 Install PyTorch

Whisper requires PyTorch.

## CPU Installation

```bash
pip install torch torchvision torchaudio
```

## GPU Installation (NVIDIA CUDA)

Visit:

https://pytorch.org/get-started/locally/

Example for CUDA 12.1:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

# 🎵 Install FFmpeg

Whisper uses FFmpeg for audio processing.

## Windows

### Step 1

Download FFmpeg from:

https://ffmpeg.org/download.html

### Step 2

Extract the ZIP file.

### Step 3

Add the FFmpeg **bin** directory to your system PATH.

Example:

```text
C:\ffmpeg\bin
```

### Step 4

Verify installation:

```bash
ffmpeg -version
```

---

## Ubuntu/Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

---

## macOS

```bash
brew install ffmpeg
```

---

# 📥 Whisper Model Download

No manual model download is required.

The model is automatically downloaded the first time the application is executed.

Example:

```python
import whisper

model = whisper.load_model("large-v3")
```

This project uses:

```python
model = whisper.load_model("large-v3")
```

> **Note:** The first execution may take several minutes because the Large-v3 model (~1.5 GB) will be downloaded automatically.

---

## 🧠 Available Whisper Models

| Model    | Size    | Speed   | Accuracy |
| -------- | ------- | ------- | -------- |
| tiny     | 39 MB   | Fastest | Low      |
| base     | 74 MB   | Fast    | Moderate |
| small    | 244 MB  | Medium  | Good     |
| medium   | 769 MB  | Slower  | Better   |
| large-v3 | ~1.5 GB | Slowest | Best     |

---

## Model Cache Locations

### Windows

```text
C:\Users\<username>\.cache\whisper
```

### Linux/macOS

```text
~/.cache/whisper
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🎧 Supported Audio Formats

* MP3
* WAV
* M4A
* OGG
* FLAC

---

# 🔄 Application Workflow

1. User uploads a Hindi audio file.
2. Audio is validated and preprocessed.
3. Audio is converted into WAV format.
4. Long audio files are split into chunks.
5. Whisper transcribes Hindi speech.
6. Whisper translates the transcription into English.
7. Results are displayed in the Streamlit UI.

---

# 🎯 Target Users

* Students
* Researchers
* Content Creators
* Journalists
* Professionals
* General Users

---

# 📸 Screenshots

Add screenshots inside a `screenshots` folder.

```text
screenshots/
├── home_page.png
├── upload_screen.png
├── transcription_output.png
└── translation_output.png
```

Example:

```markdown
![Home Screen](screenshots/home_page.png)
```

---

# 🔮 Future Enhancements

* Multi-language support.
* Real-time microphone transcription.
* Download transcription as PDF.
* Speaker diarization.
* Text summarization.
* Cloud deployment support.

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sai Jashwanth Akula**

AI Engineer | Machine Learning Engineer | Generative AI Enthusiast

---

## ⭐ If you found this project useful, please give it a star on GitHub!
