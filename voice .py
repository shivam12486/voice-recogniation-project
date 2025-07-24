import speech_recognition as sr
import pyttsx3
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and perform actions
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I help you?")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

# Perform actions based on voice
def perform_action(command):
    if "open google" in command:
        speak("Opening google")
        os.system("google-chrome https://www.google.com")

    elif "open youtube" in command:
        speak("Opening youtube")
        os.system("youtube")

    elif "open calculator " in command:
        speak("Opening calculator")
        os.system("calculator")

    elif "open brave" in command:
        speak("Opening brave")
        os.system("brave")

    elif "what is your name" in command:
        speak("I am your voice assistant.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Command not recognized. Please try again.")

# Run the assistant
while True:
    command = listen_command()
    if command:
        perform_action(command)
