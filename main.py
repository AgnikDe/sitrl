import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import os

# Initialize recognizer
recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Please say something:")
        recognizer.adjust_for_ambient_noise(source)  # Helps reduce background noise
        voice = recognizer.listen(source)

        # Convert speech to text
        text = recognizer.recognize_google(voice, language="en")
        print("You said:", text)

        # Translate text
        translator = GoogleTranslator(source="auto", target="hi")  # Auto-detect source language
        translated_text = translator.translate(text)
        print("Translated Text:", translated_text)

        # Convert text to speech
        converted_audio = gTTS(translated_text, lang="hi")  
        converted_audio.save("Hello.mp3")

        # Play the translated speech

        # playsound.playsound("Hello.mp3")
        # os.system("start Hello.mp3")  # Works on Windows
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load("Hello.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # Wait for the audio to finish
            continue



        # Alternative for Windows: os.system("start Hello.mp3")
        # Alternative for Linux: os.system("mpg321 Hello.mp3")

except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Could not request results, check your internet connection.")
except Exception as e:
    print("Error:", str(e))