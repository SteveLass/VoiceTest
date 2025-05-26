import streamlit as st
import whisper
import tempfile
import soundfile as sf
import speech_recognition as sr

# Charger le modèle Whisper une fois
model = whisper.load_model("base")  # tu peux aussi tester avec "small", "medium", ou "large"

# Fonction de transcription avec Whisper
def transcribe_with_whisper(audio_data):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(audio_data.get_wav_data())
        f.flush()
        result = model.transcribe(f.name)
        return result["text"]

# Application principale Streamlit
def main():
    st.title("🎤 Application de Reconnaissance Vocale avec Whisper")
    st.write("Appuyez sur le bouton et commencez à parler...")

    recognizer = sr.Recognizer()

    if st.button("🎙️ Démarrer l'enregistrement"):
        with sr.Microphone() as source:
            st.info("🔴 Enregistrement en cours... Parlez maintenant.")
            audio = recognizer.listen(source)
            st.info("⏳ Transcription en cours...")

            try:
                text = transcribe_with_whisper(audio)
                st.success(f"📝 Transcription : {text}")
            except Exception as e:
                st.error(f"❌ Erreur : {e}")

# Lancer l'app
if __name__ == "__main__":
    main()
