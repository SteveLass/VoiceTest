import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Parlez maintenant...")
        audio_text = r.listen(source)
        st.info("🔄 Transcription en cours...")

        try:
            text = r.recognize_google(audio_text, language="fr-FR")
            return text
        except sr.UnknownValueError:
            return "❌ Désolé, je n'ai pas compris."
        except sr.RequestError:
            return "❌ Le service Google Speech Recognition est indisponible."

def main():
    st.title("🗣️ Application de reconnaissance vocale")
    st.write("Cliquez sur le bouton ci-dessous pour commencer à parler :")

    if st.button("🎤 Commencer l'enregistrement"):
        text = transcribe_speech()
        st.write("📝 Transcription :", text)

if __name__ == "__main__":
    main()
