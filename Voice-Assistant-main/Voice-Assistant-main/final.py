import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import wolframalpha
import psutil
import math
import requests
import pyjokes
import sqlite3
from selenium import webdriver
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
# speak("I am your assistant Genie  . Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        try:
            weather_data = data["main"]
            temperature = weather_data["temp"]
            feels_like = weather_data["feels_like"]
            humidity = weather_data["humidity"]
            description = data["weather"][0]["description"]

            weather_info = f"The current temperature in {city} is {temperature}°C with {description}. It feels like {feels_like}°C with {humidity}% humidity."
            return weather_info
        except KeyError:
            return "Error: Unable to retrieve weather information. Please try again later."
    else:
        return f"Error: City '{city}' not found. Please try again with a valid city name."

def create_task(task):
    """
    Function to create a new task.
    """
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print("Task created successfully.")
    
    
def delete_task(task_id):
    """
    Function to delete an existing task.
    """
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully.")
    

def list_tasks():
    """
    Function to list all tasks.
    """
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"{task[0]} - {task[1]} - {task[2]}")
    else:
        print("No tasks found.")
        
        
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT, expense_name TEXT, amount REAL)''')
conn.commit()

def create_expense(expense_name, amount):
    """
    Function to create a new expense.
    """
    c.execute("INSERT INTO expenses (expense_name, amount) VALUES (?, ?)", (expense_name, amount))
    conn.commit()
    print("Expense created successfully.")

def list_expenses():
    """
    Function to list all expenses.
    """
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    if expenses:
        print("Expenses:")
        for expense in expenses:
            print(f"{expense[0]} - {expense[1]} - {expense[2]}")
    else:
        print("No expenses found.")

def get_voice_command():
    """
    Function to get voice command using SpeechRecognition library.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

        
            
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps")

        elif 'learn coding' in query:
            webbrowser.open("https://www.programiz.com")

        elif 'listen music' in query:
            webbrowser.open("https://www.spotify.com")

        elif 'play movie' in query:
            webbrowser.open("https://www.netflix.com")

        elif 'microsoft' in query:
            webbrowser.open("https://www.microsoft.com")

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

        elif 'booking' in query:
            webbrowser.open("https://www.makemytrip.com")

        elif 'online shopping' in query:
            webbrowser.open("https://www.flipkart.com")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")

        elif "play music" in query:
            music_dir = "C:\\Users\\HP\\Desktop\\songggg"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "open" in query:
            query = query.replace("open", "")
            query = query.replace("jarvis", "")
            webbrowser.open(query + ".com")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shailesh at D Y Patil Institute of Technology, Pimpri.")

        elif 'calculator' in query:
            speak("Sure, what calculation would you like to perform?")
            calculation = takeCommand()
            
            try:
                result = eval(calculation)
                speak(f"The result of {calculation} is {result}")
            except Exception as e:
                speak("Sorry, I couldn't perform the calculation. Please try again.")

        elif 'powerpoint presentation' in query:
            speak("Opening PowerPoint presentation")
            power = r"C:\\Users\\HP\\Desktop\\voice assistant ppt.pptx"
            os.startfile(power)

        elif "write a note" in query:
            speak("What should I write, sir")
            note = takeCommand()
            with open('jarvis.txt', 'w') as file:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            with open("jarvis.txt", "r") as file:
                print(file.read())
                speak(file.read())

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "search" in query:
            speak("What do you want to search for?")
            search_query = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            
            
        elif 'project information' in query:
            speak("OK Sir")
            speak("Project name is A I assistant for DPU students")
            speak("""Features  of  my  project  is  that my  A I Assistant offers voice commands,     voice searching, 
                  and      voice-activated device control,       letting you complete a number of tasks      . 
                  It is designed to give you conversational interactions to solve your queries and 
                  doubt regarding college issues .""")

        elif "system info" in query:
                system_stats()
                
                       
                
        elif "ok" in query:
            speak(" Thank you , Do you have any more Questions?")
            
        # Add this block inside your main loop after taking the command
        elif "weather" in query:
            speak("Sure, which city's weather would you like to know?")
            city = takeCommand()
            weather_info = get_weather(city)
            speak(weather_info)
            
        
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()

    # Create a table to store tasks
        c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
    
        # Task Management Commands
        if 'create a new task' in query or 'add task' in query or 'record a new task' in query:
            speak("Sure, what task would you like to add?")
            task = takeCommand()
            create_task(task)


        elif 'give list of task' in query or 'show task' in query or 'display task' in query:
            list_tasks()
            
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

        elif "minimise" in query:
                speak("Okay sir, minimizing the window")
                pyautogui.keyDown("win")
                pyautogui.press("m")
                pyautogui.keyUp("win")
                
                
        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
 
        elif 'add expense' in query:
            print("Please provide the name and amount for the expense.")
            name_command = get_voice_command()
            amount_command = get_voice_command()
            try:
                amount = float(amount_command.split()[-1])  # Extracting amount from the command
                expense_name = name_command
                create_expense(expense_name, amount)
            except ValueError:
                print("Invalid amount. Please try again.")
        elif 'list expenses' in query:
            list_expenses()
        elif 'exit' in query:
            print("Exiting...")
            break
        else:
            print("Command not recognized.")
