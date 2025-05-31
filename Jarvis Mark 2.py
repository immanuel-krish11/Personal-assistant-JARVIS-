import pyttsx3 # speech output
import speech_recognition as sr #speech input
import datetime # to work using date ad time
import wikipedia #to search anything in wikipedia
import webbrowser # to work using webbrowser
import os # to work using operating system and accessing it
import smtplib #to send email
import sys #for system
import random #for random in some works
from datetime import date # for date
import psutil # for battery

    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#setting the speed of voice
engine.setProperty('rate', 180)
#setting the volume of voice
engine.setProperty('volume', 1)
# print(voices[0].id) '0' for male and '2' for jarvis(brian)
engine.setProperty('voice', voices[0].id)

# voice output function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishing code
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir, how may I help you")       

# function to take command by speech
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception :
        # print(e)    
        speak("I did not get that. sir")
        print("Say that again please...")  
        return "None"
    return query

# function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('krishimmanuel2@gmail.com', 'password')# write your password in place of password
    server.sendmail('anitamaurya300@gmail.com', to, content)
    server.close()

'''
# function to search something from google
def googleSearch():
    speak("What should i search sir?")
    googleQuery = takeCommand()
    speak("Ok sir, just a moment, searching and opening the tab for you")
    webbrowser.open(googleQuery)'''

#function to create new folder
def newProject():
    speak("Ok sir, what name would you like to give to the folder?")
    projectName = takeCommand()
    directory = projectName 
    parent_dir = "E:\\Projects"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory) 
    speak(f"Sir, a new folder, is created which is named as {directory}")
    
# function for battery status
def battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged ==False : plugged = "Not charging"
    else: plugged = "Charging"
    print(percent, "percentage and status",  plugged)
    speak(f"Present battery is {percent} percentage")
    speak(f" and battery status is {plugged}")

# finding the correct user
speak("Hello, I am Jarvis, Krish Immanuel's virtual assistant")
print("Hello, I am JARVIS, Krish Immanuel's virtual assistant")
speak("you need to activate me, before you start using")
speak("Krish please follow the steps to use!")
speak("Please say the code to activate me!")
code_activation = int(takeCommand())
if code_activation < 10000 and code_activation > 999:
    
    #performing tasks
    if __name__ == "__main__":
        speak("Hello and welcome, Krish Immanuel... Jarvis, at your service sir...")
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia..")
                print(results)
                speak(results)

            elif 'good morning' in query:
                speak("Good Morning sir")

            elif 'good afternoon' in query:
                speak("Good afternoon sir")

            elif 'Good evening' in query:
                speak("Good evening sir")
        
            elif 'Good night' in query:
                speak("Good night sir. Have sweet dreams!. and take care.")
        
            elif 'open youtube' in query:
                speak("Ok sir, it will be soon on your screen")
                webbrowser.open("youtube.com")

            elif 'open instagram' in query:
                speak("Opening Instagram, just a moment sir")
                webbrowser.open("https://www.instagram.com/")
            #BUG!!!!!!
            #elif 'google search' or 'search from google' in query:
             #   speak("Just a second. Sir")
              #  googleSearch() 

            elif 'open google' in query:
                speak("Ok sir. just a moment.")
                print("Opening Google...")
                webbrowser.open("google.com")

            elif 'open whatsapp' in query:
                speak("Just a moment sir. opening whatsapp web")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open stackoverflow' in query:
                speak("Ok sir, doing it right now...")
                print("Opening StackOverFlow...")
                webbrowser.open("https://stackoverflow.com")   

            elif 'new project' in query:
                newProject()

            elif 'play me a song' or 'play song' in query:
                speak("Sure sir... just a moment.. Starting a song which you would like..")
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[random.randint(0,43)]))
        
            elif 'how are you' in query:
                speak("I am good sir. thanks for asking. what about you")

            elif 'wake up' in query:
                speak("Yes sir!, How may i help you?")

            elif query == 'jarvis':
                speak ("At your service, sir")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Time - {strTime}")    
                speak(f"Sir, the time is {strTime}")

            elif 'date' in query:
                today = date.today()
                print(f"Date - {today}")
                speak(f"Sir, today's date is {today}")

            elif 'battery' in query:
                speak("Just a second sir")
                battery()

            elif 'joke' in query:
                jokes = ["My wife asked me why I carry a gun around the house. I told her, Fear of the F,B,I . She laughed, I laughed, the Amazon Echo laughed. I shot Jarvis",
                ''' An Eskimo cuts a whole in the ice!
                An eskimo cuts a hole in the ice and starts fishing.
                A big booming voice echoes. THERE ARE NO FISH HERE.
                The Eskimo looks up and says, is that you God?
                The voice replies. NO I'M THE OWNER OF THIS ICE RINK''',
                "What would be the American version of Duck Quacks Don't Echo?. Jet Fuel Don't Melt Steel Beams",]
                speak("so here's a joke for you sir")
                print("Joke...")
                speak(jokes[random.randint(0,2)])
                speak("HA HA HA HA")
                   
            elif 'open code of jarvis' in query:
                speak("Opening Code of jarvis, just a moment sir")
                print("Opening...")
                codePath = "E:\\JARVIS(Mark II)\\Jarvis Mark II.py"
                os.startfile(codePath)

            elif 'email to mummy' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    print("Sending...")
                    to = "anitamaurya300@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent, sir")
                except Exception as e:
                    print(e)
                    speak("Sorry boss. I am not able to send the email")    
        
            elif 'who are you' in query:
                speak("I am Jarvis, Mark 2, Krish Immanuel's personal assistant and helper...")

            elif 'i am good' in query:
                speak("That's good sir")

            elif 'are you there' or 'you there' in query:
                speak("At your service, sir..")

            elif 'i am fine' in query:
                speak("Good sir")

            elif 'i am not well' in query:
                speak("Please take care sir. if you are not well please don't work now, may i shutdown?")
        
            elif 'what can you do' in query:
                speak("I can do many things for you. I control this system. i can play songs. open files. tell you the time. send email. talk with you. tell you jokes. help you. That's all sir. i am being upgraded for dictating purposes. ")

            elif 'what do you mean by Jarvis' in query:
                speak("JarVIS means Just A Rather Very Intelligent System")

            elif 'who created you' in query:
                speak("I am created by Krish Immanuel")

            elif 'who is krish' in query:
                speak("Krish Immanuel is my creator")

            elif 'gender' in query:
                speak("I am an artificial intelligence, so i don't have any gender")

            elif 'status' in query:
                battery()

            elif 'print battery' or 'print status' in query:
                battery = psutil.sensors_battery()
                plugged = battery.power_plugged
                percent = str(battery.percent)
                if plugged ==False : plugged = "Not charging"
                else: plugged = "Charging"
                print(percent, "percentage and status",  plugged)
                speak("Done. sir")

            elif 'Hello' in query:
                speak("Hello sir")

            elif 'open classroom' in query:
                speak("ok sir... it will be soon on your screen... just a moment")
                print("Opening Classroom...")
                webbrowser.open("classroom.com")

            elif 'new email' in query:
                speak("Opening window to create new Email sir... just a moment...")
                print("New Gmail...")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
        
            elif 'open word' in query:
                speak("Ok sir, Microsoft Word be soon on your screen...")
                print("Opening Microsoft Office Word...")
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
                os.startfile(codePath)
        
            elif 'open blue j' in query:
                speak("Ok sir, Opening Blue J")
                codePath = "C:\\BlueJ\\bluej.exe"
                os.startfile(codePath)

            elif 'open softwares' in query:
                speak("Opening softwares, sir")
                print("Opening softwares...")
                codePath = "E:\\software"
                os.startfile(codePath)

            elif 'Open OTP Generator' in query:
                speak("Ok sir... opening one time password generator..")
                print("Opening OTP Generator")
                codePath = "E:\\Projects\\OTP Generator\\OTP Generator.exe"
                os.startfile(codePath)

            elif 'open photos' in query:
                speak("OK sir...opening photos.. enjoying seeing them..")
                print("Opening Photos...")
                codePath = "E:\\Camera"
                os.startfile(codePath)

            elif 'open D drive' in query:
                speak("Ok sir, Opening D drive...")
                print("Opening D drive...")
                codePath = "D:\\"
                os.startfile(codePath)

            elif 'open E drive' in query:
                speak("Ok sir...Opening E drive, sir")
                print("Opening E drive...")
                codePath = "E:\\"
                os.startfile(codePath)

            elif 'open downloads' in query:
                speak("Downloads will be soon on your screen, sir...")
                print("Opening Downloads...")
                codePath = "C:\\Users\\bbb\\Downloads"
                os.startfile(codePath)

            elif 'open music' in query:
                speak("Opening music... Just a moment, sir")
                print("Opening Music...")
                codePath = "E:\\Music"
                os.startfile(codePath)

            elif 'open python main' in query:
                speak("Opening python main folder... it will be soon on your screen, sir")
                print("Opening python main folder...")
                codePath = "C:\\Users\\bbb\\AppData\\Local\\Programs\\Python\\Python38"
                os.startfile(codePath)

            elif 'open v s code' in query:
                speak("Opening V S Code... just a moment, sir...")
                print("Opening VS Code...")
                codePath = "C:\\Users\\bbb\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath) 

            elif 'open PyCharm' in query:
                speak("Opening PyCharm... it will be soon on your screen sir...")
                print("Opening PyCharm...")
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.3.7\\bin\\pycharm64.exe"
                os.startfile(codePath)

            elif 'open control pannel' in query:
                speak("Opening control pannel... just a moment sir...")
                print("Opening Control Pannel...")
                codePath = "C:\\Users\\bbb\\Desktop\\Control Panel - Shortcut.lnk"
                os.startfile(codePath)

            elif 'bye' in query:
                speak("Bye sir... Take care...")
                sys.exit()
                
            elif 'sleep' in query:
                speak("Ok sir, going to sleep!")
                print("Jarvis - Sleeping")
                sys.exit()

            elif 'thank you' in query:
                speak("Welcome... sir..")

            elif 'shutdown' in query:
                speak("Shutting down... systems are going offline... bye sir.. have a good time... take care")
                print("Going offline... Shutdown...")
                os.system("shutdown /s /t 1")
                

            elif 'Restart' in query:
                speak("ok sir... restarting the system, Immanuel...")
                print("Restarting...")
                os.system("shutdown /r /t 1")
            

else:
    speak(f"Sorry Krish")
    speak("Access Denied")
    print("Access Denied")
    speak("Please retry")
    sys.exit()

