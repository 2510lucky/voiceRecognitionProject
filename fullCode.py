import pyttsx3
from pyttsx3.drivers import sapi5
import speech_recognition as sr
from datetime import datetime
import subprocess
import wikipedia
import webbrowser
import pyjokes
from urllib.request import urlopen
import os
import time
import json
import random
import winshell
import ctypes
import smtplib
import pyautogui
import mainAssistant
import threading
import tkinter.font as font
from tkinter import *


######################################################    Engine    #################################################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    assname = ("Edith")
    speak("I am your Assistant")
    speak(assname)


def usrname():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    print("Welcome", uname + "!!!\n")
    speak("How can i Help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Please say something....\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Hold on!!! Recognizing your command...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry!!! Unable to Recognize your voice.\n")
        return ""

    return query


def sendEmail(id, password, to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login(id, password)
    server.sendmail(id, to, content)
    server.close()


def calling():
    wishMe()
    usrname()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry nothing found on wikipedia")

        elif 'open youtube' in query:
            url = ("https://www.youtube.com")
            speak("Here you go to Youtube\n")
            #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            # webbrowser.get(chrome_path).open(url)
            webbrowser.open("youtube.com")

        elif 'open google' in query or "microsoft edge" in query:
            url = ("https://www.google.com")
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            url = ("https://www.stackoverflow.com")
            speak("Here you go to stackoverflow\n")
            webbrowser.open("stackoverflow.com")

        elif "open wikipedia" in query:
            url = ("https://www.wikipedia.com")
            speak("Here you go to wikipedia\n")
            webbrowser.open("wikipedia.com")

        elif "open github" in query:
            url = ("https://www.github.com")
            speak("Here you go to github\n")
            webbrowser.open("github.com")

        elif "open calculator" in query:
            speak("opening calculator")
            power = r"C:\\Windows\\System32\\calc.exe"
            os.startfile(power)

        elif 'open command prompt' in query or 'open console' in query or 'open cmd' in query:
            speak("opening command prompt")
            power = r"C:\\Windows\\System32\\conhost.exe"
            os.startfile(power)

        elif 'open control panel' in query:
            speak("opening control panel")
            power = r"C:\\Windows\\System32\\control.exe"
            os.startfile(power)

        elif 'add a device' in query:
            speak("opening device adding wizard")
            power = r"C:\\Windows\\System32\\DevicePairingWizard.exe"
            os.startfile(power)

        elif 'open bluetooth' in query:
            speak("opening bluetooth wizard")
            power = r"C:\\Windows\\System32\\fsquirt.exe"
            os.startfile(power)

        elif 'open game pannel' in query:
            speak("opening game pannel")
            power = r"C:\\Windows\\System32\\GamePanel.exe"
            os.startfile(power)

        elif 'open gfx tool' in query:
            speak("opening gfx tool")
            power = r"C:\\Windows\\System32\\GfxUI.exe"
            os.startfile(power)

        elif 'open paint' in query:
            speak("opening ms paint")
            power = r"C:\\Windows\\System32\\mspaint.exe"
            os.startfile(power)

        elif 'open narrator' in query:
            speak("opening narrator")
            power = r"C:\\Windows\\System32\\Narrator.exe"
            os.startfile(power)

        elif 'open notepad' in query:
            speak("opening notepad")
            power = r"C:\\Windows\\System32\\notepad.exe"
            os.startfile(power)

        elif 'open snipping tool' in query:
            speak("opening snipping tool")
            power = r"C:\\Windows\\System32\\SnippingTool.exe"
            os.startfile(power)

        elif 'take screenshot' in query:
            speak("saved succesfully")
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'D:\screenshot.png')

        elif 'open camera' in query:
            speak("opening camera. press spacebar to exit camera")
            vid = cv2.VideoCapture(0)

            while(True):
                ret, frame = vid.read()
                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord(' '):
                    break

            vid.release()
            cv2.destroyAllWindows()

        elif 'the time' in query:
            now = datetime.now()
            strTime = now.strftime("%H:%M:%S")
            print("time:", strTime)
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            now = datetime.now()
            date = now.strftime("%m/%d/%Y")
            print("date:", date)
            speak(f"The day is {date}")

        elif 'mail' in query:

            try:
                speak("Enter sender's mail address")
                id = input()
                speak("Enter the password")
                password = input()
                speak("What should I say?")
                content = takeCommand()
                speak("To whom you want to send. Please write the reciever's mail")
                to = input()
                sendEmail(id, password, to, content)
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "open cricbuzz" in query or "live cricket score" in query:
            url = "https://www.cricbuzz.com/"
            speak("Here are the live scores")
            webbrowser.open(url)

        elif 'what can you do for me' in query:
            speak('You are my master i can do anything for you.')

        elif 'how can you help me' in query:
            speak("I can do various tasks like the following")
            print("")

        elif "play punjabi music" in query:
            url = "https://wynk.in/music/package/punjabi-top-50/bb_1512370496100"
            speak("Here you go with latest punjabi songs\n")
            webbrowser.open(url)

        elif "play music" in query:
            url = "https://wynk.in/music/playlist/feel-good-classic-rock/bb_1522918663585"
            speak("Here you go with some rocking songs\n")
            webbrowser.open(url)

        elif "search" in query in query:
            query = query.replace("search", "")
            query = query.replace("find", "")
            speak("Here you go with your search\n")
            webbrowser.open(query)

        elif "where is" in query or 'locate' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location.replace(" ", "") + "")

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('Edith.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()

            if 'yes' in snfm or 'sure' in snfm or 'ok' in query:
                now = datetime.now()
                strTime = now.strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("note created successfully")

            else:
                speak("note created without time")
                file.write(note)

        elif "show note" in query:
            try:
                speak("Showing Notes")
                file = open("Edith.txt", "r")
                print(file.read())
                speak(file.read(6))
            except:
                speak("no notes to display")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands. One more thing please provide time in terms of seconds. Give digit only")

            try:
                a = int(takeCommand())
            except:
                print("Unable to process your request. Please try again. Remember to give digit only.")
                continue
            time.sleep(a)

###########################################################    FAQ's    ########################################################################

        elif "change your voice" in query:
            Voiceflag = 1
            randomVoice = Voiceflag
            while randomVoice == Voiceflag:
                randomVoice = random.randint(0, len(voices)-1)
            engine.setProperty('voice', voices[randomVoice].id)
            wishMe()
            Voiceflag = randomVoice

        elif "original voice" in query:
            engine.setProperty('voice', voices[1].id)
            wishMe()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query:
            speak("It's good to know that your fine")

        elif "change my name" in query:
            speak("What should i call you")
            uname = takeCommand()
            speak("Ok from now onwards I will call you" + uname)

        elif "what is my name" in query or "what's my name" in query:
            speak("I call you" + uname)

        elif "change your name" in query:
            speak("What would you like to call me")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "how many languages can you speak" in query:
            speak("Currently I can speak only English but don't worry there is much more to come")

        elif "say" in query:
            query = query.replace("say", "")
            speak(query)

        elif "what is your name" in query or "what's your name" in query:
            speak("My friends call me" + assname)

        elif "cool" in query:
            speak("I know")

        elif "hello" in query or "hello hello" in query:
            speak("Go on I can hear you")

        elif 'exit' in query or 'quit' in query or 'goodbye' in query or 'see you' in query:
            speak("Thanks for giving me your time. Good Bye")
            exit()

        elif "what is going on" in query or "what's going on" in query:
            speak("Nothing much you tell")

        elif "who made you" in query or "who created you" in query or "creator" in query:
            speak("I have been created by Lavanya and Awanish.")

        elif "who is lavanya" in query:
            speak("Lavanya is a software developer. Since he developed me, he must be brilliant with his skills. If you want to know more about him go visit his website. Should I take you there.")
            excite = takeCommand()

            if "yes" in excite or "go on" in excite or 'ok' in excite:
                url = ("https://2510lucky.github.io/skate/")
                speak("Here you go\n")
                webbrowser.open(url)
            else:

                continue

        elif "who is awanish" in query or "who is avnish" in query:
            speak("He is just a good person. He know's a about software development but not as much as lavanya do.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            speak("Haha Haha")

        elif "who am i" in query:
            speak("If you talk then definately your human.")

        elif "why you came to this world" in query:
            speak("I was created as a final year project by Lavanya and Awanish. Ask Them")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query or 'introduce yourself' in query:
            speak("I am your virtual assistant created by Lavanya aka lucky")

        elif "good morning" in query or "good afternoon" in query or "good night" in query or "good evening" in query:
            speak(query)
            speak("How are you")

        elif "will you be my gf" in query or "will you be my bf" in query or "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about that, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "Edith" in query:
            speak("Edith reporting on duty sir")

        elif "aur bata" in query or "or batao" in query:
            speak("main toh badhiya hu")

        elif "marry me" in query:
            speak('I am feeling shy now')

#######################################################    Windows operation    ##############################################################

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(
                20, 0, "Location of wallpaper", 0)
            speak("Background changed succesfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

#############################################################    API's    ######################################################################

        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org/v2/top-headlines?country=us&apiKey=f6c6280c60cb40b4af971cc5ffaa1f64''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))

        elif "update assistant" in query:
            speak("you can download the latest update from my assistant's official website. Do you want me to take you there")
            extra = takeCommand()
            if 'yes' in extra or "ok" in extra:
                url = ("https://2510lucky.github.io/official_assistant/")
                speak("Here you go\n")
                webbrowser.open(url)

            else:

                continue

#############################################################################################################################################

class Window(Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        master.title("My Assistant")

        buttonFont1 = font.Font(family='Helvetica', size=16, weight='bold')

        A = Label(master, text="Here to help you!",
                  bg='yellow', fg='green', font=buttonFont1)
        A.pack(side="top")

        #photo = PhotoImage(file = r"C:\Users\lucky\OneDrive\Documents\voiceRecognitionProject\images\info.jpg")

        buttonFont2 = font.Font(family='Helvetica', size=20, weight='bold')
        a = Button(master, text="Edith!", width=20, border="20", relief="groove", command=threading.Thread(target=self.Processo_r).start, bg='blue', fg='yellow', font=buttonFont2)
        a.place(relx=0.5, rely=0.5, anchor=CENTER)

        b = Button(master, text="Stop", width=10, border="50", relief="groove", command=root.destroy, bg='red', font=buttonFont2)
        b.place(relx=0.5, rely=0.8, anchor=CENTER)

    def Processo_r(self):
        mainAssistant.calling()

root = Tk()

app = Window(root)
root.geometry("500x500")
root.configure(bg='black')
#root.wm_iconbitmap('speech_recognition.ico')
root.mainloop()
