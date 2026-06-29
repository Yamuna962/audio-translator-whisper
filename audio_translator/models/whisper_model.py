import whisper
import streamlit as st

from audio_translator.config import WHISPER_MODEL


@st.cache_resource
def load_whisper_model():

    return whisper.load_model(
        WHISPER_MODEL
    )
