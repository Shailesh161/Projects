 import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyautogui
import smtplib
import psutil
import math
import requests
import time
from time import sleep 
import pyjokes
import pywhatkit
import noisereduce

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])

def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    print("System status is :")
    print(final_res) 
    speak(final_res)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("PBL    project       2023 of  shailesh       ,       tejas   ,   swapnil     ,   amit   and    mrunal at      D Y Patil   Institute   of      Technology,Pimpri")       
    speak("I am your assistant Genie  . Please tell me how may I help you")  
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    print(city, state,country)
    speak(city)
    speak(state)
    speak(country)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google search' in query:
            speak('this is I found for your search')
            query=query.replace('DYPIAN'," ")
            query=query.replace ('google search'," ")
            pywhatkit.search(query)
            speak('done sir')
        
        
        elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  

        elif 'open map' in query:
            webbrowser.open("maps.google.com")
        
        elif 'youtube search ' in query:
            query=query.replace('DYPIAN'," ")
            query=query.replace ('youtube search'," ")
            web = 'https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            speak("done sir!")
        
        elif "jokes" in query:
             joke=pyjokes.get_joke(language='en', category= 'neutral')
             speak(joke)
        elif 'project' in query:
            speak("OK Sir")
            speak("Project name is A I assistant for DPU students")
            speak("Team members are amit,tejas,shailesh,swapnil,mrunal ")
            speak("""Features of Our project is that Our A I Assistant offers voice commands,voice searching, 
                  and voice-activated device control, letting you complete a number of tasks . 
                  It is designed to give you conversational interactions to solve your queries and 
                  doubt regarding college issues .""")
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        
        elif "system info" in query:
                system_stats()

        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
 
        elif 'learn coding' in query:
            webbrowser.open("programiz.com")
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()


        elif 'powerpoint presentation' in query:
            speak("opening Power Point presentation")
            power = r"S:\project\voice assistant ppt.pptx"
            os.startfile(power) 

        elif 'pbl' in query:
         os.startfile("S:\project\PBL FINAL PR.docx")

        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'calculator' in query:
            webbrowser.open("calculator.com")

        elif 'booking' in query:
            webbrowser.open("makemytrip.com")

        elif 'online shopping' in query:
            webbrowser.open("flipkart.com")
        
        # windows shortcut keys 
        elif "switch the window" in query or "switch window" in query  :
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(0.5)
                pyautogui.keyUp("alt")
        
        elif  "close window" in query  :
                speak("Okay sir, Closing the window")
                pyautogui.keyDown("Ctrl")
                pyautogui.press("W")
                time.sleep(0.5)
                pyautogui.keyUp("Ctrl")

        elif "increase volume" in query  :
                speak("Okay sir, increasing the volume")
                pyautogui.keyDown('volumeup')
                time.sleep(1.0)
                pyautogui.keyUp('volumeup')
        
        elif "volume stop" in query  :
                speak("Okay sir, I am switching to mute mode ")
                pyautogui.hotkey('volumemute')

        elif "restore" in query:
                speak("Okay sir, restoring the window")
                pyautogui.keyDown("win")
                pyautogui.keyDown("shift")
                pyautogui.press("m")
                pyautogui.keyUp("win")
                pyautogui.keyUp("shift")
       
        elif "lock" in query:
                speak("Okay sir, locking the pc")
                pyautogui.hotkey('win', 'r') 
                pyautogui.typewrite("cmd\n") 
                sleep(0.500)       
                pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")      

        elif "minimise" in query:
                speak("Okay sir, minimizing the window")
                pyautogui.keyDown("win")
                pyautogui.press("m")
                pyautogui.keyUp("win")
       
        #college info
        elif "erp" in query or 'erp portal' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://campus.dpuerp.in/Secured/DashBoardStudent.aspx")
       
        elif "Admission" in query or 'Admission process' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/ugadmissions.aspx")

        elif "college" in query or 'Profile' in query or 'college profile' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/college-profile.aspx")

        elif "computer engineering" in query or 'computer branch' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/computer-engineering.aspx") 


        elif "Academics" in query :
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/Acadmic-Calender.aspx")

        elif "Training and placement" in query :
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/from-the-desk-of-tpo.aspx")

        elif "Computer engineering placements" in query or 'placement' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/placements.aspx")

        elif "University rankers" in query or 'Toppers' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/university-rankers.aspx")

        elif "mission" in query or 'vision' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/vision-mission.aspx")

        elif "Computer engineering faculty" in query or 'faculty ' in query or ' staff ' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/computer-engineering-faculty-and-staff.aspx")

        elif 'open code' in query:
            codePath = "A:\my codes\proejct"
            os.startfile(codePath)
        
        elif "my location" in query:
            speak("Your current locationis :")
            my_location() 
        
        

        elif 'shutdown' in query:
           speak("shutting down")
           os.system("shutdown /s /t 1")
           
        
        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
