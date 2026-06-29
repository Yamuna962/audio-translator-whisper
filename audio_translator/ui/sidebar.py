import streamlit as st

from audio_translator.config import (
    APP_TITLE,
    LOGO_PATH
)


def render_sidebar():

    with st.sidebar:

        if LOGO_PATH:

            try:
                st.image(
                    LOGO_PATH,
                    use_container_width=True
                )

            except:
                pass

        st.title(APP_TITLE)

        st.markdown("---")

        st.markdown(
            """
### Features

- Hindi Speech Recognition
- English Translation
- Whisper AI
- Streamlit Interface

---
"""
        )

        st.info(
            "Upload a Hindi audio file to begin."
        )
