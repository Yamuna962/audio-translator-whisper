def render_upload_section():

    st.header("Upload Audio File")

    audio_file = st.file_uploader(
        "Upload a Hindi audio file",
        type=["mp3", "wav", "m4a", "ogg"],
        key="audio_uploader"
    )

    if audio_file is None:
        return None

    current_hash = get_file_content_hash(audio_file)

    is_new_file = (
        current_hash !=
        st.session_state.file_content_hash
    )

    if is_new_file:

        cleanup_previous_audio()
        reset_transcription_state()

        with st.spinner(
            "Processing uploaded audio..."
        ):

            audio_path = process_uploaded_file(
                audio_file
            )

            if audio_path:

                st.session_state.current_audio_path = (
                    audio_path
                )

                st.session_state.file_content_hash = (
                    current_hash
                )

                st.success(
                    "Audio loaded successfully!"
                )

    if (
        st.session_state.current_audio_path and
        os.path.exists(
            st.session_state.current_audio_path
        )
    ):

        st.audio(
            st.session_state.current_audio_path,
            format="audio/wav"
        )

    return st.session_state.current_audio_path
