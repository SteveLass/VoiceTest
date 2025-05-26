import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile

def transcribe_audio_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="fr-FR")
            return text
        except sr.UnknownValueError:
            return "❌ Je n'ai pas compris l'audio."
        except sr.RequestError:
            return "❌ Service Google Speech Recognition indisponible."

def main():
    st.title("🗣️ Transcription audio (via fichier)")
    st.write("Téléversez un fichier audio (.wav ou .mp3) pour obtenir la transcription.")

    uploaded_file = st.file_uploader("🎵 Fichier audio", type=["wav", "mp3"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            # Convertir en .wav au cas où c'est un .mp3
            audio = AudioSegment.from_file(uploaded_file)
            audio.export(tmp.name, format="wav")

            # Transcription
            text = transcribe_audio_file(tmp.name)
            st.success("✅ Transcription réussie")
            st.write("📝", text)

if __name__ == "__main__":
    main()
