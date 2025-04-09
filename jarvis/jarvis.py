import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #setup speech recoging
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #for david voice

def speak(audio):
    """Function to speak the given audio"""
    engine.say(audio)
    engine.runAndWait()

def wish_me(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("WELCOME BACK MR SHUKLA \nhow can i help you")

def take_command(): #for on microphone and turn into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "None"
    return query.lower()



if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()

        if 'wikipedia' in query or 'who' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Multiple results found. {e.options}")
                speak("Multiple results found. Please specify your query.")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
        
        elif 'there' and 'alive' in query:
            speak("at your service sir")
    
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Archit\\Music\\jana'
            songs =os.listdir(music_dir)
            if songs:
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                print("No music files found in the specified directory.")
                speak("No music files found in the specified directory.")

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open vs' in query:
            speak("sir,I M opening VS Code")
            code_path = "C:\\Users\\Archit\\AppData\\Local\\Programs\\Microsoft VS"
            os.startfile(code_path)

        elif 'open excel' in query:
            speak("opening MS Excel")
            code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(code_path)

        elif 'open chrome' in query:
            speak("opening google chrome")
            code_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(code_path)
        
        elif 'thank you' in query or 'thanks' in query:
            speak("ANY time, Sir")
            print("Any time, Sir")

        elif 'shutdown' in query:
            speak("I M OUT")
            print("jarvis is offline now!")
            exit()

