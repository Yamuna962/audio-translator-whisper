import os

from audio_translator.utils.audio_utils import (
    split_audio,
    safe_transcribe
)


def transcribe_audio(model, audio_path):

    hindi_text = ""
    english_text = ""

    chunks = split_audio(audio_path)

    for chunk in chunks:

        result_hi = safe_transcribe(
            model=model,
            audio_path=chunk,
            language="hi",
            fp16=False
        )

        result_en = safe_transcribe(
            model=model,
            audio_path=chunk,
            task="translate",
            fp16=False
        )

        if result_hi and "text" in result_hi:
            hindi_text += result_hi["text"] + " "

        if result_en and "text" in result_en:
            english_text += result_en["text"] + " "

        if (
            chunk != audio_path and
            os.path.exists(chunk)
        ):
            os.remove(chunk)

    return {

        "hindi": hindi_text.strip(),

        "english": english_text.strip()

    }
