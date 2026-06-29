import hashlib
import os
import shutil
import tempfile

from pydub import AudioSegment

from audio_translator.config import TEMP_DIR


# ----------------------------------
# Validate uploaded audio
# ----------------------------------

def validate_audio_content(uploaded_file):

    if uploaded_file is None:
        return False

    if uploaded_file.size == 0:
        return False

    return True


# ----------------------------------
# Hash uploaded file
# ----------------------------------

def get_file_content_hash(uploaded_file):

    uploaded_file.seek(0)

    file_hash = hashlib.md5(
        uploaded_file.read()
    ).hexdigest()

    uploaded_file.seek(0)

    return file_hash


# ----------------------------------
# Save uploaded file
# ----------------------------------

def process_uploaded_file(uploaded_file):

    if not validate_audio_content(uploaded_file):
        return None

    suffix = os.path.splitext(
        uploaded_file.name
    )[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
        dir=TEMP_DIR
    ) as temp_file:

        shutil.copyfileobj(
            uploaded_file,
            temp_file
        )

        return temp_file.name


# ----------------------------------
# Split Audio
# ----------------------------------

def split_audio(audio_path):

    """
    Currently returns a single chunk.

    Later we can split long audio
    into 30-second chunks.
    """

    return [audio_path]


# ----------------------------------
# Whisper Wrapper
# ----------------------------------

def safe_transcribe(
    model,
    audio_path,
    **kwargs
):

    try:

        return model.transcribe(
            audio_path,
            **kwargs
        )

    except Exception as e:

        print(e)

        return None


# ----------------------------------
# Cleanup temp file
# ----------------------------------

def cleanup_temp_files():

    if not os.path.exists(TEMP_DIR):
        return

    for file in os.listdir(TEMP_DIR):

        path = os.path.join(
            TEMP_DIR,
            file
        )

        try:

            if os.path.isfile(path):

                os.remove(path)

        except:

            pass


# ----------------------------------
# Cleanup previous audio
# ----------------------------------

def cleanup_previous_audio():

    cleanup_temp_files()
