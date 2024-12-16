from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    playsound("response.mp3")


# this tts sounds horrible --> maybe use open ai tts api