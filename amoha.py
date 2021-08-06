import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

import os
import smtplib
import subprocess
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("good evening!")

    speak("I am Amoha mam! How may i help you??")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('choudharymuskan141001@gmail.com','password')
    server.sendmail('choudharymuskan141001@gmail.com',to,content)
    server.close()

def takecommand():
    '''
    it takes microphone input and returns string input
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)
         

        try:
            print("recognizing..")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")
        except Exception as e:
            #print(e)
            print('say that again please')
            return"None"
        return query



if __name__=="__main__":
    #speak("Hello Musky! Hope you doing well")
    wishMe()
    

    
    while True:
    
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open linkedin' in query:
            webbrowser.open("https://in.linkedin.com/")
        
        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")
        

        elif 'open whatsapp' in query:
            webbrowser.open_new_tab('https://web.whatsapp.com')
        
        
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        
        elif 'open prime' in query:
            webbrowser.open("https://www.primevideo.com/")

        elif 'open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    
        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        

        elif 'open netflix' in query:
            webbrowser.open('https://www.netflix.com/in/')
        
        
        
        elif 'play music' in query:
            music_dir='C:\\Users\\user\\Music'
            songs=os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,random.choice(songs)))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'mam ,the time is{strTime}')
        
        elif 'open visual studio' in query:
            VSPath="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(VSPath)

        elif 'open atom' in query:
            VSPath="C:\\Users\\user\\AppData\\Local\\atom\\atom.exe"
            os.startfile(VSPath)

        elif "send email" in query:
             try:
                 speak("What should i say?")
                 content=takecommand()
                 to="choudharymuskan141001@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent!!")
             except Exception as e:
                speak('Sorry Musky I am not able to send email!!')
         









 
