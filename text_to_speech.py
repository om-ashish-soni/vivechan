from gtts import gTTS
import pygame
from pydub import AudioSegment
from util import generate_unique_audio_filename,delete_temp_audio
from pydub.playback import play
import soundfile as sf
from scipy import signal
import streamlit as st
import base64

playback_speed=1.5

def speak(text):
    filename=generate_unique_audio_filename()
    print("filename",filename)

    try:
        tts = gTTS(text, lang='en', slow=False)
        tts.save(filename)

        # # Open the audio file in binary mode and read its content
        # with open(filename, 'rb') as audio_file:
        #     audio_bytes = audio_file.read()

        # # Display the audio file in Streamlit
        # st.audio(audio_bytes, format='audio/ogg')

        with open(filename, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                    <audio controls autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                    </audio>
                    <script>
                        var audio = document.querySelector('audio');
                        audio.playbackRate = {playback_speed};
                    </script>
                    """
            st.markdown(
                md,
                unsafe_allow_html=True,
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")

    