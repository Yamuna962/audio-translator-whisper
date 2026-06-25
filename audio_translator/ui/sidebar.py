import os
import streamlit as st

from audio_translator.config import LOGO_PATH

def render_sidebar():

    with st.sidebar:

        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=280)

        st.title("🎤 Hindi Audio → English Translator")

        st.markdown("---")

        st.info("""
        Upload Hindi audio

        Get English transcription instantly
        """)