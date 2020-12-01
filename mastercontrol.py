import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import random
import time
import pyautogui
from googlesearch import search
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

print("Initializing master control 1.0")
engine.setProperty('voice',voices[0].id)
keyword="master control"
battery = psutil.sensors_battery()
percent = str(battery.percent)
percentst = 'Battery level currently at '+percent+' percent'
plugged = battery.power_plugged
plugged = 'This device is currently plugged in and charging' if plugged else 'This device is currently not plugged in and slowly discharging'
source_loc='sahakar nagar parvati paytha'

def credentials():
    for i in range (0,30):
        print('###',end='')
    username = input("\n\nEnter your username / email : ")
    for i in range (0,30):
        print('+-+',end='')
    password = input("\n\nEnter your password : ")
    for i in range (0,30):
        print('###',end='')
    ch = input("\nDo you want to continue with this username and password (y/n) : ")
    for i in range (0,30):
        print('###',end='')

def clear():
    os.system('cls')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if(hour>=0 and hour<=12):
        speak('Good morning sir')
    elif(hour>=12 and hour<=16):
        speak('Good afternoon sir')
    else:
        speak('Good Evening sir')
    speak(plugged)
    speak(percentst)
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        clear()

        try:
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-in')
            #print(query)
            clear()
        except Exception as e:
            speak('Could you repeat that please?')
            query=takeCommand().lower()
            return query
        return query
    
def hotkeycheck():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        clear()

        try:
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-in')
            #print(query)
            clear()
        except Exception as e:
            query=hotkeycheck().lower()
            return query
        return query

wishMe()
active_flg=0
name="Dwoom"
user="Hi "+name+". I will be happy to assist you today"
speak("Tell me what to do")
user2="You are "+name+" and I am your personal assistant"
while True:
    activate = hotkeycheck().lower()
    print(activate)
    if 'master control' in activate:
        speak('yes sir? What would you like me to do?')
        active_flg=1
        while active_flg==1:
            query = takeCommand().lower()
            
# User Intro
            if 'am I' in query:
                speak(user2)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Assistant Intro
            elif 'your name' in query:
                speak("I am master control, your personal assistant")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wikipedia Summary reader
            elif 'wikipedia' in query or 'what is' in query:
                speak('On it, give me a few')
                query=query.replace('wikipedia','')
                query=query.replace('what is','')
                query=query+" wikipedia"
                for link in search(query, tld="co.in",num=1, stop=1, pause=2):
                    webbrowser.open(link)
                    break
                query=query.replace('wikipedia','')
                results='So wikipedia says that'+wikipedia.summary(query, sentences=3)
                speak(results)
                speak('You can read further on this page')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#TODO : Google search logic

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Volp
            elif 'volp' in query:
                webbrowser.open('https://classroom.volp.in/')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Whatsapp web
            elif 'whatsapp' in query:
                speak("Opening whatsapp web")
                webbrowser.open('https://web.whatsapp.com/')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Internshala
            elif 'internshala' in query:
                speak('Opening Internshala')
                webbrowser.open('https://internshala.com/student/dashboard?referral=header')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Spotify
            elif 'spotify' in query:
                speak('Sure')
                os.startfile('C:\\Users\\Dell\\AppData\\Roaming\\Spotify\\Spotify.exe')
                speak('Playing last played track in queue')
                time.sleep(3)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Close spotify
            elif 'stop' in query:
                os.close('C:\\Users\\Dell\\AppData\\Roaming\\Spotify\\Spotify.exe')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Battery level
            elif 'battery' in query:
                speak(plugged)
                speak(percentst)      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Google site open        
            elif 'open' in query or 'go to' in query:
                query=query.replace('open','')
                query=query.replace('go to','')
                statement="Opening "+query
                speak(statement)
                for link in search(query, tld="co.in",num=1, stop=1, pause=2):
                    webbrowser.open(link)
                    break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Play music via Youtube       
            elif 'play' in query :
                query=query.replace('play','')
                query=query.replace('some','')
                query=query+" youtube"
                statement="Playing "+query
                speak(statement)
                for link in search(query, tld="co.in",num=1, stop=1, pause=2):
                    webbrowser.open(link)
                    break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Launch any app     
            elif 'launch' in query :
                query=query.replace('launch','')
                query=query.replace('please','')
                query=query.replace('could you','')
                pyautogui.press('win')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Google Maps
            elif 'where is' in query or 'locate' in query:
                    query = query.replace('where is', '')
                    query = query.replace('locate','')
                    query = query.replace('for me','')
                    location = query
                    ask = 'Do you want me to give you the location for '+location+'?'
                    speak(ask)
                    confirm=takeCommand()
                    if 'yes' in confirm or 'yeah' in confirm:
                        directions = 'Do you want directions to this location?'
                        speak(directions)
                        confirmdir=takeCommand()
                        if 'yes' in confirmdir or 'yeah' in confirmdir:
                            current_loc = 'Current location is set to '+source_loc+'. Would you like to continue with this location or change it?'
                            speak(current_loc)
                            get_curr_loc = takeCommand()
                            if 'yes' in get_curr_loc or 'continue' in get_curr_loc:
                                speak('Getting directions')
                                webbrowser.open('https://www.google.co.in/maps/dir/'+source_loc+'/'+location+'')
                            elif 'no' in get_curr_loc or 'change' in get_curr_loc or 'different' in get_curr_loc:
                                speak('Say the new location name now please')
                                source_loc=takeCommand()
                                speak('Getting directions')
                                webbrowser.open('https://www.google.co.in/maps/dir/'+source_loc+'/'+location+'')
                        elif 'no' in confirmdir:
                            webbrowser.open('https://www.google.co.in/maps/place/' + location + '')
                    elif 'no' in confirm:
                        speak('Okay, what else can I do for you?')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # master control dormant mode
            elif 'goodbye' in query or 'thank you master control' in query or "that's all" in query or 'that will be all' in query:
                speak('Bye dwoom')
                active_flg=0
                break
        # Deactivate master control
            elif 'deactivate' in query:
                break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif 'deactivate' in activate:
        speak('master control going offline')
        break

    
