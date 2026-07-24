import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import pyttsx3
import schedule
import time
import threading
import webbrowser
import os
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

import speech_recognition as sr
import sounddevice as sd
import soundfile as sf

def listen():
    device = 1

    # Use the microphone's default sample rate
    info = sd.query_devices(device, 'input')
    fs = int(info['default_samplerate'])

    print("🎤 Speak now...")

    audio = sd.rec(
        int(5 * fs),
        samplerate=fs,
        channels=1,
        dtype='int16',
        device=device
    )

    sd.wait()

    sf.write("voice.wav", audio, fs)

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile("voice.wav") as source:
            audio_data = recognizer.record(source)

        command = recognizer.recognize_google(audio_data)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("No internet connection.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""

def reminder(msg):
    speak("Reminder")
    speak(msg)

def set_reminder():
    speak("Enter reminder time in HH:MM format")
    reminder_time = input("Time (HH:MM): ")

    speak("Enter reminder message")
    message = input("Reminder: ")

    schedule.every().day.at(reminder_time).do(reminder, message)

    speak("Reminder has been set")

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler, daemon=True).start()

speak("Hello! I am your Voice Assistant. How can I help you today?")


while True:
    command = listen()

    if command is None:
        continue

    if "time" in command:
        speak(datetime.now().strftime("%I:%M %p"))

    elif "date" in command:
        speak(datetime.now().strftime("%d %B %Y"))

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "calculator" in command:
        os.system("calc")

    elif "notepad" in command:
        os.system("notepad")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I didn't understand.")