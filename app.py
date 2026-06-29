import streamlit as st

from audio_translator.ui.sidebar import render_sidebar
from audio_translator.ui.upload_section import render_upload_section
from audio_translator.ui.about_section import render_about

from audio_translator.utils.session_utils import (
    initialize_session_state
)

from audio_translator.models.whisper_model import (
    load_whisper_model
)

from audio_translator.services.transcription_service import (
    transcribe_audio
)

from audio_translator.config import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

initialize_session_state()

render_sidebar()

left, right = st.columns([3,1])

with left:

    audio_path = render_upload_section()

    if (
        audio_path
        and
        not st.session_state.processing_complete
    ):

        with st.spinner("Transcribing..."):

            model = load_whisper_model()

            results = transcribe_audio(
                model,
                audio_path
            )

            st.session_state.transcription_results = (
                results
            )

            st.session_state.processing_complete = True

    if st.session_state.transcription_results:

        st.subheader("Hindi Transcription")

        st.write(
            st.session_state.transcription_results[
                "hindi"
            ]
        )

        st.subheader("English Translation")

        st.write(
            st.session_state.transcription_results[
                "english"
            ]
        )

with right:

    render_about()
