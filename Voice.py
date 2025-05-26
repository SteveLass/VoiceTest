import streamlit as st
import speech_recognition as sr

def transcribe_speech_with_index(mic_index):
    r = sr.Recognizer()
    try:
        mic = sr.Microphone(device_index=mic_index)
    except Exception as e:
        return f"Failed to access microphone device {mic_index}: {e}"

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=10)  # optional: adjust for ambient noise
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            text = r.recognize_google(audio_text)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."

 except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

def main():
    st.title("Speech Recognition App")
    st.write("Select your microphone and click the button to start recording:")

    mic_names = sr.Microphone.list_microphone_names()
    mic_index = st.selectbox(
        "Choose Microphone Device",
        options=range(len(mic_names)),
        format_func=lambda i: f"{i}: {mic_names[i]}"
    )

    if st.button("Start Recording"):
        transcription = transcribe_speech_with_index(mic_index)
        st.write("Transcription:", transcription)

if _name_ == "_main_":
    main()
