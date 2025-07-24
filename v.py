import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
    except:
        speak("Sorry, I didn't catch that.")
        return ""
    return query

def run_assistant():
    speak("Hi, I am your AI assistant. How can I help you?")
    while True:
        command = take_command().lower()
        if "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
        elif "stop" in command:
            speak("Goodbye Shivam!")
            break

run_assistant()