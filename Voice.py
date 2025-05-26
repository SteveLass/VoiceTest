import streamlit as st
from streamlit_audio_recorder import audio_recorder
import speech_recognition as sr
import tempfile
from pydub import AudioSegment
import uuid

def transcribe_wav(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio, language="fr-FR")
        except sr.UnknownValueError:
            return "❌ Je n'ai pas compris."
        except sr.RequestError:
            return "❌ Service Google indisponible."

def main():
    st.set_page_config(page_title="🎤 Transcription Vocale", layout="centered")
    st.title("🎙️ Transcription vocale en ligne")
    st.markdown("Appuyez sur le bouton ci-dessous pour enregistrer votre voix, puis cliquez sur **Transcrire**.")

    # Génère une clé unique à chaque chargement pour éviter les conflits DOM
    component_key = str(uuid.uuid4())

    audio_bytes = audio_recorder(
        text="Cliquez pour enregistrer",
        icon_size="2x",
        key=component_key  # 👈 clé dynamique
    )

    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        if st.button("Transcrire"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_bytes)
                tmp_path = tmp.name

            text = transcribe_wav(tmp_path)
            st.success("✅ Transcription réussie")
            st.write("📝", text)

if __name__ == "__main__":
    main()
