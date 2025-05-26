import streamlit as st
import speech_recognition as sr

# Fonction de transcription vocale
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Parlez maintenant...")
        audio_text = r.listen(source)
        st.info("⏳ Transcription en cours...")

        try:
            text = r.recognize_google(audio_text, language="fr-FR")
            return text
        except:
            return "❌ Désolé, je n'ai pas compris."

# Fonction principale Streamlit
def main():
    st.title("🗣️ Application de Reconnaissance Vocale")
    st.write("Appuyez sur le bouton ci-dessous et parlez dans le micro.")

    if st.button("🎙️ Démarrer l'enregistrement"):
        text = transcribe_speech()
        st.success(f"📝 Transcription : {text}")

# Lancement de l'application
if __name__ == "__main__":
    main()
