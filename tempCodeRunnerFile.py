import pyaudio
import wave
import os
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import wikipedia
from selenium import webdriver
import os
import tkinter as tk
import time
import wave
import pywhatkit as pwt
import webbrowser
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        print("elenor:good morning sir")
        speak("good moring sir")
    elif(hour>=12 and hour<18):
        print("elenor:good afternoon sir")
        speak("good afternoon sir")
    elif(hour>18 and hour<20):
        print("elenor:good evening sir")
        speak("good evening sir")
    else:
        print("elenor:good night sir")
        speak("good night sir ")
    print("elena:i am elenor how can i help you")
    speak("i am elenor how can i help you")

# Record audio
def record_audio(filename, duration=5, chunk=1024, channels=1, rate=44100):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("listening...")

    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("recognizing.")

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

# Recognize speech from recorded audio using Google Speech Recognition API
def recognize_speech(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("user:", text.lower())
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Error fetching results from Google Speech Recognition")
        except AttributeError as e:
            pass
global c
if __name__=="__main__":
      while 1:
        try:   
            
         query = "recorded_audio.wav"
         record_audio(query)
         query=recognize_speech(query).lower()   
         if("alina"in query or "ali"in query):
            query = "recorded_audio.wav"
            record_audio(query)
            query=recognize_speech(query).lower()   
            print("user:")
            if(query=='stop'):
                raise StopIteration
            if("hello"in query or "hello ele"in query or "yoo"in query or "hello elena"in query):
               wishme()
               del query
               query = "recorded_audio.wav"
               record_audio(query)
               query=recognize_speech(query)        
            elif("wikipedia"in query ):
                speak("searching wikipedia")
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia..")
                print(f"user:{result}")  
                speak(result)
                break
            elif("open google"in query ):
                  url="google.com"
                  print("elena:opening google sir")
                  speak("opening goodle")
                  chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                  webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
                  webbrowser.get("chrome").open_new_tab(url)
                  break
            elif("open youtube"in query):
                  url="youtube.com"
                  print("elena:opening youtube sir")
                  speak("opening youtube sir")
                  chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                  webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
                  webbrowser.get("chrome").open_new_tab(url)
                  break
            elif("open open ai"in query):
                 url="openai.com"
                 print("elena:opening openai sir")
                 speak("opening open a i")
                 chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                 webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
                 webbrowser.get("chrome").open_new_tab(url)
                 break
                 record_audio(ch)
            elif("calculate"in query or"calculator"in query):
                print("elena:what do you want to calculate ?")
                speak("what do you want to calculate")
                dict = {"zero":0,"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
                ch = "recorded_audio.wav"
                record_audio(ch)
                ch=recognize_speech(ch).lower()
                ch1= "recorded_audio.wav"
                record_audio(ch1)
                ch1=recognize_speech(ch1).lower()
                ch2= "recorded_audio.wav"
                record_audio(ch2)
                ch2=recognize_speech(ch2).lower()
                a=int(dict[ch])
                b=int(dict[ch2])
                match(ch1):
                    case "plus":
                         print(f"elena{a+b}")
                         speak(a+b)
                         break
                    case '+':
                         print(f"elena:{a+b}")
                         speak(a+b)
                         break
                    case "minus":
                       print(f"elena:{a-b}")
                       speak(a-b)
                       break
                    case '_':
                      print(f"elena:{a-b}")
                      speak(a-b)
                      break
                    case "multiplied":
                       print("elena:{a*b}")
                       speak(a*b)
                       break
                    case '*':
                         print(f"elena:{a*b}")
                         speak(a*b)
                         break
                    case "divide":
                        try:
                          print(f"elena:{a/b}")
                          speak(a/b)
                        except ZeroDivisionError as e:
                           print("elena:please sir tell some other number")
                           speak("please sir tell some other number")
                    case '/':
                        try:
                           print(f"elena:{a/b}")
                           speak(a/b)
                        except ZeroDivisionError as e:
                             print("elena:please sir tell some other number")
                             speak("please sir tell some other number")
                             break
            elif("atomic habites summary"in query):
                print("elena:here is summary of atomic habit")
                f= open("hello1.txt","r")
                speak(f.read())
                break
            elif("what time"in query):
                t=datetime.datetime.now()
                t1=t.strftime("%H:%M:%S")
                print("elenor:"+t1)
                speak(t1)
                break
            elif("whats today date"in query):
                t=datetime.datetime.now()
                t1=t.strftime("%D-%M-%Y")
                print("elenor:"+t1)
                speak(t1)
                break
            if("dot"in query):
                raise StopIteration
            if("play"in query):
                query = "recorded_audio.wav"
                record_audio(query)
                query=recognize_speech(query).lower()   
                print(f"elenor:playing video of "+query)
                speak("playing video of "+query)
                c=pwt.playonyt(query)
                break
            elif("open vs code"in query or("start vs code"in query)):
                url="C:\\Users\\User\\AppData\\Local\\Programs\M\\icrosoft VS Code\\Code.exe"
                os.startfile(url)
                break
            elif("open intelligent idea"in query):
                url="C:\\Program Files\\JetBrains\\IntelliJ IDEA 2023.2.1\\bin\\idea64.exe"
                os.startfile(url)
                break
            if("open github"in query):
                 url="https://github.com/"
                 print("elena:opening github sir")
                 speak("opening github sir")
                 chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                 webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
                 webbrowser.get("chrome").open_new_tab(url)
                 break
            webbrowser.quit()
            
        except StopIteration as e:
            break 