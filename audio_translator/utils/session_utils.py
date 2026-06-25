import streamlit as st

def initialize_session_state():

    defaults = {
        "current_audio_path": None,
        "transcription_results": {},
        "last_file_id": None,
        "processing_complete": False,
        "file_content_hash": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value