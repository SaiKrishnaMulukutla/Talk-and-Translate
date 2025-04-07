import streamlit as st
import speech_recognition as spr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import os

st.set_page_config(page_title="Talk & Translate 🗣️✨", page_icon="🗣️", layout="centered")

recognizer = spr.Recognizer()
mc = spr.Microphone()

def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        recognized_text = recog.recognize_google(audio)
        return recognized_text
    except spr.UnknownValueError:
        st.error("Google Speech Recognition could not understand the audio.")
        return None
    except spr.RequestError as ex:
        st.error(f"Could not request results from Google Speech Recognition service; {ex}")
        return None

language_map = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Kannada': 'kn', 'Tamil': 'ta',
    'Malayalam': 'ml', 'Bengali': 'bn', 'German': 'de', 'Chinese': 'zh-CN',
    'Japanese': 'ja', 'Arabic': 'ar', 'Italian': 'it', 'Korean': 'ko'
}

st.title("Talk & Translate 🗣️🔁")
st.markdown("""
This application captures your speech, detects the language, translates it, and then converts it back to speech in the target language. 
Choose the source and target language, then click the "Start Speaking" button to begin.
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    source_language_input = st.selectbox("Select the source language:", list(language_map.keys()), index=0)

with col2:
    target_language_input = st.selectbox("Select the target language:", list(language_map.keys()), index=1)

source_language_code = language_map[source_language_input]
target_language_code = language_map[target_language_input]

if st.button("Start Speaking", use_container_width=True):
    with st.spinner("Listening... Please speak now!"):
        with mc as source:
            MyText = recognize_speech(recognizer, source)

    if MyText:
        st.success(f"Recognized Text: {MyText}")
        try:
            detected_language = detect(MyText)
            st.write(f"Detected Language: {detected_language}")

            if not os.path.exists('outputs'):
                os.makedirs('outputs')

            translated_text = GoogleTranslator(source=detected_language, target=target_language_code).translate(MyText)
            st.write(f"Translated Text in {target_language_input}: {translated_text}")

            speak = gTTS(text=translated_text, lang=target_language_code, slow=False)
            audio_file = f"outputs/captured_voice_{target_language_input}.mp3"
            speak.save(audio_file)

            st.audio(audio_file, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
    else:
        st.warning("No speech detected. Please try again!")

else:
    st.info("Click the button to start the voice recognition and translation process.")

st.markdown("""
---
Developed with ❤️ by Mulukutla Sai Krishna.
""")
