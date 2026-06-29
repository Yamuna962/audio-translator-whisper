import os
import streamlit as st

from audio_translator.config import SAMPLE_ZIP_PATH


def render_about():

    st.markdown("### About The Tool")

    st.markdown("""
    This tool transcribes Hindi audio into text
    and provides English translation.
    """)

    st.markdown("### Target Personas")

    st.markdown("""
    - Students
    - Researchers
    - Professionals
    - Content Creators
    """)

    st.markdown("### Download Sample Files")

    if os.path.exists(SAMPLE_ZIP_PATH):

        with open(SAMPLE_ZIP_PATH, "rb") as f:

            st.download_button(
                label="📥 Download Sample ZIP",
                data=f,
                file_name="sample_audio.zip",
                mime="application/zip"
            )

    else:
        st.warning("Sample ZIP file not found.")
