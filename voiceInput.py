# using speech_recognition needs pyaudio and portaudio
import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the microphone as the source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        # print("You said: " + text)

    except sr.UnknownValueError:
        text = "Google Speech Recognition could not understand audio"
        # print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        text = "Could not request results from Google Speech Recognition service"
        # print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text
