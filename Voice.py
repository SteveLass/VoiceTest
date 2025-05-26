import streamlit as st
import speech_recognition as sr
def transcribe_speech() :
    # Initialisation de la classe de reconnaissance
    r = sr.Recognizer()
    # Lecture du microphone comme source
    avec sr.Microphone() comme source :
        st.info("Parlez maintenant..." ;)
        # écoute la parole et la stocke dans la variable audio_text
        audio_text = r.listen(source)
        st.info("Transcription..." ;)

        essayer :
            # utiliser la reconnaissance vocale de Google
            text = r.recognize_google(audio_text)
            return text
        except :
            return "Désolé, je n'ai pas compris." ;
            def main() :
    st.title("Speech Recognition App" ;)
    st.write("Cliquez sur le microphone pour commencer à parler:" ;)

    # ajouter un bouton pour déclencher la reconnaissance vocale
    if st.button("Start Recording" ;):
        text = transcribe_speech()
        st.write("Transcription : " ;, text)
if __name__ == "__main__" :
    main()
