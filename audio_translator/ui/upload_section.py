import os
import streamlit as st

from audio_translator.config import (
    SUPPORTED_FORMATS
)

from audio_translator.utils.audio_utils import (

    process_uploaded_file,

    get_file_content_hash,

    cleanup_previous_audio

)

from audio_translator.utils.session_utils import (

    reset_transcription_state

)


def render_upload_section():

    st.header("🎵 Upload Audio")

    uploaded_file = st.file_uploader(

        "Upload Hindi Audio",

        type=SUPPORTED_FORMATS

    )

    if uploaded_file is None:

        return st.session_state.current_audio_path

    file_hash = get_file_content_hash(uploaded_file)

    if file_hash != st.session_state.file_content_hash:

        cleanup_previous_audio()

        reset_transcription_state()

        with st.spinner("Processing audio..."):

            audio_path = process_uploaded_file(

                uploaded_file

            )

        if audio_path:

            st.session_state.current_audio_path = audio_path

            st.session_state.file_content_hash = file_hash

            st.success("✅ Audio uploaded successfully.")

    if (

        st.session_state.current_audio_path

        and

        os.path.exists(

            st.session_state.current_audio_path

        )

    ):

        st.audio(

            st.session_state.current_audio_path

        )

    return st.session_state.current_audio_path
