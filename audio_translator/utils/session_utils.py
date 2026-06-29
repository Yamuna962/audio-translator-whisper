import streamlit as st

from audio_translator.utils.audio_utils import (
    cleanup_previous_audio
)


def initialize_session_state():

    defaults = {

        "current_audio_path": None,

        "file_content_hash": None,

        "processing_complete": False,

        "transcription_results": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def reset_transcription_state():

    st.session_state.processing_complete = False

    st.session_state.transcription_results = None


def reset_all():

    cleanup_previous_audio()

    st.session_state.current_audio_path = None

    st.session_state.file_content_hash = None

    st.session_state.processing_complete = False

    st.session_state.transcription_results = None
