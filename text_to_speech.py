from gtts import gTTS
import pygame
from pydub import AudioSegment
from util import generate_unique_audio_filename,delete_temp_audio
from pydub.playback import play
import soundfile as sf
from scipy import signal
import streamlit as st
import base64
import io

playback_speed=1.5

def speak(text):
    # filename=generate_unique_audio_filename()
    # print("filename",filename)

    try:
        tts = gTTS(text, lang='en', slow=False)
        
        
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)  # Move the pointer to the start of the BytesIO object
        b64 = base64.b64encode(mp3_fp.read()).decode('utf-8')

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

        ## OLD LOGIC OF FILE

        # tts.save(filename)

        # with open(filename, "rb") as f:
        #     data = f.read()
        #     b64 = base64.b64encode(data).decode()
        #     md = f"""
        #             <audio controls autoplay="true">
        #             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        #             </audio>
        #             <script>
        #                 var audio = document.querySelector('audio');
        #                 audio.playbackRate = {playback_speed};
        #             </script>
        #             """
        #     st.markdown(
        #         md,
        #         unsafe_allow_html=True,
        #     )
        #     delete_temp_audio(filename)


    except Exception as e:
        st.error(f"An error occurred: {e}")

    