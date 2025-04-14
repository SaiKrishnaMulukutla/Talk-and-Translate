import streamlit as st
import speech_recognition as spr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
import os

st.set_page_config(page_title="Talk & Translate 🗣️✨", page_icon="🗣️", layout="centered")

recognizer = spr.Recognizer()

language_map = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Kannada': 'kn', 'Tamil': 'ta',
    'Malayalam': 'ml', 'Bengali': 'bn', 'German': 'de', 'Chinese': 'zh-CN',
    'Japanese': 'ja', 'Arabic': 'ar', 'Italian': 'it', 'Korean': 'ko'
}

st.title("Talk & Translate 🗣️🔁")
st.markdown("""
This application captures your **uploaded speech**, detects the language, translates it, and converts it to speech in the target language.  
Upload an audio file (WAV/MP3), select languages, and let the app do the rest!
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    source_language_input = st.selectbox("Select the source language:", list(language_map.keys()), index=0)

with col2:
    target_language_input = st.selectbox("Select the target language:", list(language_map.keys()), index=1)

source_language_code = language_map[source_language_input]
target_language_code = language_map[target_language_input]

uploaded_audio = st.file_uploader("Upload an audio file (WAV/MP3):", type=["wav", "mp3"])

if uploaded_audio is not None:
    st.audio(uploaded_audio, format='audio/wav')
    
    with st.spinner("Transcribing..."):
        try:
            # Use AudioFile to process uploaded audio
            with spr.AudioFile(uploaded_audio) as source:
                audio_data = recognizer.record(source)
                MyText = recognizer.recognize_google(audio_data)

            st.success(f"Recognized Text: {MyText}")
            
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

        except spr.UnknownValueError:
            st.error("Speech Recognition could not understand the audio.")
        except spr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Upload an audio file to begin the voice recognition and translation process.")

st.markdown("""---  
Developed with ❤️ by Mulukutla Sai Krishna.
""")
