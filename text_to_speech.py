from gtts import gTTS
import pygame
from pydub import AudioSegment
from util import generate_unique_audio_filename,delete_temp_audio
from pydub.playback import play
import soundfile as sf
from scipy import signal

def speak(text):
    filename=generate_unique_audio_filename()
    print("filename",filename)

    tts = gTTS(text, lang='en', slow=False)
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(20)
    pass

    