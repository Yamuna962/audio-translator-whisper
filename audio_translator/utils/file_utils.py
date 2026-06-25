import hashlib
import os
import streamlit as st


def get_file_content_hash(uploaded_file):
    """
    Generate SHA256 hash for uploaded file.
    Used to detect whether the user uploaded a new file.
    """

    if uploaded_file is not None:
        uploaded_file.seek(0)
        file_bytes = uploaded_file.read()
        uploaded_file.seek(0)

        return hashlib.sha256(file_bytes).hexdigest()

    return None


def cleanup_previous_audio():
    """
    Delete previously processed audio file.
    """

    path = st.session_state.current_audio_path

    if path and os.path.exists(path):
        try:
            os.unlink(path)
        except Exception:
            pass

    st.session_state.current_audio_path = None


def reset_transcription_state():
    """
    Reset all transcription-related session variables.
    """

    st.session_state.transcription_results = {}
    st.session_state.processing_complete = False