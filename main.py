import datetime
import os
import subprocess
import webbrowser as wb
from subprocess import Popen
from typing import Any
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
from time import sleep
import pyautogui
import tkinter
import pyaudio

top = tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
voicespeed = 180
engine.setProperty('rate', voicespeed)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.recognizers
    with sr.Microphone(0) as source:
        print("Listening.........")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognising....")
        Query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        print(e)
        return "-----"

    return Query


def time():
    Time = datetime.datetime.now().strftime('%I%M%p')
    speak(Time)
    # print(time)


def date():
    Day = int(datetime.datetime.now().day)
    Month = int(datetime.datetime.now().month)
    Year = int(datetime.datetime.now().year)
    speak('The current date is')
    print(Day, Month, Year)
    speak(Day)
    speak(Month)
    speak(Year)


def wishme():
    speak("welcome back sir")

    hour = datetime.datetime.now().hour
    if 6 <= hour <= 12:
        speak("Good Morning")

    elif 12 <= hour <= 18:
        speak("good Afternoon")

    elif 18 <= hour <= 24:
        speak("Good Evening")

    else:
        speak("how can I help you")


def open_chrome():
    url = "https://www.google.co.in/"
    wb.get(chrome_path).open(url)


if __name__ == '__main__':
    wishme()

    while True:
        query = take_command().lower()
        print(query)

        if "good morning" in query:
            speak("Good Morning sir")

        if "time" in query:
            time()

        elif 'date' in query:
            date()

        # open_chrome
        elif 'open chrome' in query:
            open_chrome()
        # elif 'close chrome' in query:
        #     chrome.termina
        # wikipedia
        elif 'wikipedia' in query:
            speak('Searching....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            print(result)
        # chrome_search
        elif 'search' in query:
            speak("what should I search?")
            search = take_command().lower()
            wb.get(chrome_path).open_new(search + ".com")

        # Launch an application
        elif "open notepad" in query:
            speak("opening notepad")
            location = "C:/windows/system32/notepad.exe"
            notepad: Popen[bytes] | Popen[Any] = subprocess.Popen(location)

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()

        # Random joke
        elif "joke" in query:
            speak(pyjokes.get_joke())

        # logout/ restart/ shutdown
        elif "logout" in query:
            speak('Logging out in 5 seconds')
            sleep(5)
            os.system("shutdown - l")

        elif "Shutdown" in query:
            speak('Shutting down in 5 seconds')
            sleep(5)
            os.system("shutdown /s /t ")

        elif "restart" in query:
            speak('restarting in 5 seconds')
            sleep(5)
            os.system("shutdown /r /t 1")

        # <------------------------------Pyautogui Features ----------------------------------->
        elif "start menu" in query:
            pyautogui.hotkey('win')

        elif "hidden menu" in query:
            # Win + X : open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            pyautogui.hotkey('winleft', 'tab')

        elif "take a screenshot" in query:
            pyautogui.hotkey('winleft', 'prtsc')
            speak('done')

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif 'close the app' in query:
            pyautogui.hotkey('alt', 'f4')

        elif "new desktop" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'd')
            speak('done')

        elif "desktop 1" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'left')
            speak('done')

        elif "desktop 2" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'right')
            speak('done')

        elif 'desktop' in query:
            pyautogui.hotkey('win', 'd')

        elif "clipboard" in query:
            pyautogui.hotkey('winleft', 'v')

        elif "notification" in query:
            pyautogui.hotkey('winleft', 'a')

        elif "change" in query:
            pyautogui.hotkey('alt', 'tab')
            speak('done')

        elif "search" in query:
            pyautogui.hotkey('winleft', 's')

        elif "minimise" in query:
            pyautogui.hotkey('winleft', 'm')

        elif "select all" in query:
            pyautogui.hotkey('ctrl', 'a')

        elif "copy" in query:
            pyautogui.hotkey('ctrl', 'c')

        elif "paste" in query:
            pyautogui.hotkey('ctrl', 'v')
        #
        # elif "itunes" in query:
        #     speak('opening Itunes')
        #     location2 = "D:\iTunes\iTunes.exe"
        #     itunes = subprocess.Popen(location2)
        #
        # elif "close itunes" in query:
        #     speak("closing Itunes")
        #     itunes.terminate()

        # elif "close zoom" in query:
        # speak("closing zoom")
        #     zoom.terminate()
        #
        # elif "d" in query:
        #     speak("opening D")
        #     location3 = "D:/"
        #     handtrack = subprocess.Popen(location3)
