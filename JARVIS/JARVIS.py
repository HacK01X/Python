#########

__author__ = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 0.1'

"""
JARVIS:
- Control windows programs with your voice
"""

# import modules
from datetime import datetime  # datetime module supplies classes for manipulating dates and times
import subprocess  # subprocess module allows you to spawn new processes
from playsound import *  #for sound output
import speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..
import datetime #For greeting the user

# pip install pyttsx3                  
# need to run only once to install the library

# importing the pyttsx3 library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)
    
    
#for audio output instead of print
def voice(p):
    myobj=gTTS(text=p,lang='en',slow=False)
    myobj.save('try.mp3')
    playsound('try.mp3')

# For greeting the user, by datetime module
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("This is your pc sir, please tell me how are you")
    
# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio, language = 'en-IN', show_all = True )
print(Query)


# Run Application with Voice Command Function
def get_app(Q):
    master
    if Q == "time":
        print(datetime.now())
        x=datetime.now()
        voice(x)
    elif Q == "notepad":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "browser":
        subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
=======

    apps = {
    "time": datetime.now(),
    "notepad": "Notepad.exe",
    "calculator": "calc.exe",
    "stikynot": "StikyNot.exe",
    "shell": "powershell.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "browser": "C:\Program Files\Internet Explorer\iexplore.exe"
    }

    for app in apps:
        if app == Q.lower():
            subprocess.call([apps[app]])
            break
    master
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()
    return
# Call get_app(Query) Func.
get_app(Query)


# For opening websites
if __name__ == "__main__":
    WishMe()
    query = takecommand().lower()

    if "wikipedia" in query:
        speak("searching wikipedia")
        query = query.replace("Wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stack overflow' in query:
        webbrowser.open('stackoverflow.com')
    else:
        pass
#Just like this(above) more websites can be added as well
