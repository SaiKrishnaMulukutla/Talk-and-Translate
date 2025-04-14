import streamlit as st
import speech_recognition as spr
from deep_translator import GoogleTranslator
from langdetect import detect
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile

st.set_page_config(page_title="Talk & Translate 🗣️✨", page_icon="🗣️", layout="centered")

recognizer = spr.Recognizer()

language_map = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Kannada': 'kn', 'Tamil': 'ta',
    'Malayalam': 'ml', 'Bengali': 'bn', 'German': 'de', 'Chinese': 'zh-CN',
    'Japanese': 'ja', 'Arabic': 'ar', 'Italian': 'it', 'Korean': 'ko'
}

st.title("Talk & Translate 🗣️🔁")
st.markdown("""
Upload an audio file (MP3/WAV), then select languages to translate speech into another language!
""")

col1, col2 = st.columns([1, 1])
with col1:
    source_language_input = st.selectbox("Select the source language:", list(language_map.keys()), index=0)
with col2:
    target_language_input = st.selectbox("Select the target language:", list(language_map.keys()), index=1)

source_language_code = language_map[source_language_input]
target_language_code = language_map[target_language_input]

uploaded_audio = st.file_uploader("Upload an audio file (MP3/WAV):", type=["mp3", "wav"])

if uploaded_audio is not None:
    st.audio(uploaded_audio, format="audio/mp3")

    with st.spinner("Processing audio..."):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
                audio = AudioSegment.from_file(uploaded_audio)
                audio.export(temp_wav.name, format="wav")

                with spr.AudioFile(temp_wav.name) as source:
                    audio_data = recognizer.record(source)
                    MyText = recognizer.recognize_google(audio_data)

            st.success(f"Recognized Text: {MyText}")

            detected_language = detect(MyText)
            st.write(f"Detected Language: {detected_language}")

            translated_text = GoogleTranslator(source=detected_language, target=target_language_code).translate(MyText)
            st.write(f"Translated Text in {target_language_input}: {translated_text}")

            if not os.path.exists("outputs"):
                os.makedirs("outputs")

            tts = gTTS(text=translated_text, lang=target_language_code)
            output_file = f"outputs/translated_{target_language_input}.mp3"
            tts.save(output_file)
            st.audio(output_file, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Upload an audio file to get started.")

st.markdown("""---  
Developed with ❤️ by Mulukutla Sai Krishna.
""")
