# Talk & Translate 🗣️✨
---
## Description
---
**Talk & Translate** is an innovative web application that leverages **speech recognition** and **translation technologies** to provide real-time speech translation and text-to-speech functionality. The app captures your spoken words, detects the language, translates it into the target language, and then converts the translated text back into speech. This project is designed to facilitate communication between individuals who speak different languages and enhance accessibility for non-native speakers.

The system uses popular machine learning models, APIs, and libraries to deliver seamless translation and speech synthesis. Whether you're traveling, learning a new language, or interacting with people from different cultural backgrounds, **Talk & Translate** makes communication easy and efficient.

## Home Page
---
<img width="960" alt="Image" src="https://github.com/user-attachments/assets/88312ea4-b5a1-439e-9b7b-3b4c2298b096" />

## Demo Video
---
🎥 **Watch the demo video** to see how Talk & Translate works in action!  
https://github.com/user-attachments/assets/a5021951-73ed-4ccf-8633-72792ad30b7c

## Key Features
---
- **Real-Time Speech Recognition:** Transcribes spoken words into text instantly.
- **Language Detection:** Detects the language of the spoken words with high accuracy.
- **Accurate Translation:** Translates the recognized speech into your target language.
- **Text-to-Speech:** Converts the translated text back to speech in the target language.
- **Multiple Language Support:** Offers translation and speech synthesis in over 10 languages.
- **User-Friendly Interface:** Simple and intuitive design for a seamless user experience.

## Process
---
1. **Speech Recognition:** Uses the `speech_recognition` library to capture and recognize spoken words.
2. **Language Detection:** The `langdetect` library is used to identify the language of the speech.
3. **Translation:** The recognized speech is translated using the `deep_translator` library.
4. **Text-to-Speech Conversion:** The `gTTS` (Google Text-to-Speech) library is used to convert the translated text into speech.
5. **Web Interface:** The interface is designed with **Streamlit** for easy interaction.  
6. **Model Deployment:** The app allows users to interact with the model, making it both functional and interactive.

## Technologies Used
---
- **Python:** The primary programming language for model development, speech recognition, and web application.
- **Streamlit:** Framework for creating the web-based user interface.
- **Speech Recognition (`speech_recognition`):** Used for real-time speech recognition and transcription.
- **Google Text-to-Speech (`gTTS`):** Converts translated text into speech.
- **Deep Translator:** Provides accurate translation capabilities for multiple languages.
- **Langdetect:** Used for detecting the language of the recognized speech.
- **Flask:** Used for handling backend tasks, serving API requests, and running the app.
- **Pandas & NumPy:** For data preprocessing and organizing the collected data, if applicable.

## Process Flow
---
1. **User Interaction:** The user selects a source and target language.
2. **Speech Input:** The user clicks the "Start Speaking" button, which starts the speech recognition process.
3. **Speech Recognition:** The app transcribes the user's spoken words into text.
4. **Language Detection:** The system automatically detects the language of the speech.
5. **Translation:** The recognized text is translated into the target language.
6. **Text-to-Speech:** The translated text is then converted into audio, which can be played directly through the web interface.

## Acknowledgements
---
We would like to thank the **speech recognition community**, **translation APIs**, and **open-source contributors** who provided valuable resources and tools that helped in the development of this project.
---

## Contact

For any inquiries or questions, please feel free to contact us at:  
📧 **Email:** (mailto:saikrishnamulukutla@gmail.com)
---

## Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Talk-Translate.git
   cd Talk-Translate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
