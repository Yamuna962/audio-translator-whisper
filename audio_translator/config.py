import os

# ----------------------------
# Application
# ----------------------------

APP_TITLE = "Audio Translator"

# Whisper model
# Supported: tiny, base, small, medium, large
WHISPER_MODEL = "large"

# ----------------------------
# Assets
# ----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SAMPLE_DIR = os.path.join(BASE_DIR, "sample_files")

TEMP_DIR = os.path.join(BASE_DIR, "temp")

os.makedirs(TEMP_DIR, exist_ok=True)

LOGO_PATH = os.path.join(
    ASSETS_DIR,
    "Logo_TechOptima_update.png"
)

SAMPLE_ZIP_PATH = os.path.join(
    SAMPLE_DIR,
    "sample_audio_files.zip"
)

SUPPORTED_FORMATS = [
    "mp3",
    "wav",
    "m4a",
    "ogg"
]
