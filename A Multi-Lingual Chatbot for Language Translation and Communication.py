from cgitb import text
from re import T
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from tkinter import *
import webbrowser
import requests
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver
from googletrans import Translator
from playsound import playsound
import pandas as pd

translator = Translator()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

teg=["namaskar Ram","Karam","namaskaram","namaha kharam"]
hig=["namaste","Namahste","Namah stay"]
mrg=["namaskar"]
eng=["hello","hi","hey"]
tag=["Vanakkam"]
bbb=["radhe radhe", "Radhe Radhe"]
r = sr.Recognizer()
with sr.Microphone() as source:
    print("listening")
    audio = r.listen(source)
    print("ok")
audio_text=r.recognize_google(audio,language='en-IN')
print(audio_text)

braj = ['आपकौ', 'राधे राधे', 'तुम्हारौ', 'अच्छौ', 'बहौत', 'आपकौ', 'मेरौ', 'मिलंगे', 'अच्छौ', 'कृपा', 'अँगरेजी', 'हम्बै', 'माफ़', 'नाँय', 'करतौ', 'रुकियो', 'बधाई', 'कभउ', 'बाजारों', 'भाई', 'कपड़ों', 'बरसात', 'कीमतौं', 'किधर', 'उनको', 'जायेगा', 'बच्चौ', 'जाता', 'छूता', 'होता', 'इस', 'पढ़ने', 'संख्या', 'प्रदर्शित', 'मुझे', 'आप', 'कहाँ', 'जायेगी', 'क्या', 'आती', 'ज्यादा', 'चलती', 'शहर', 'जरिये', 'सस्ता', 'गर्मियों', 'से']
hibb = ["आपका","नमस्ते", "तुम", "अच्छा", "बहुत", "आप का", "मेरा", "मिलेंगे", "अच्छा", "कृपय", "अंग्रेज़ी", "हाँ", "क्षमा", "नहीं", "करता", "रुको", "शुभकामनायें", "कभी भी", "बजारन", "भैया", "लत्तांन", "मेह", "कीमतंन", "कितकूँ", "बिन्नै", "जाबैगौ", "बच्चन", "जामतौ", "छीमतौ", "हैमतौ", "या", "पढ़बे", "गिनती", "दरशामतैं", "हाँ", "तुम", "कितकूँ", "जावैगी", "काह", "आमत", "अधिक", "चलत", "नगर", "द्वारा", "सुलभ", "गरमीन", "ते"]
lg=''
vc=''
d=''
if audio_text in eng:
    vc="en-IN"
    lg="en"
elif audio_text in hig:
    vc="hi-IN"
    lg="hi"
elif audio_text in mrg:
    vc="mr-IN"
    lg="mr"
elif audio_text in tag:
    vc="ta-IN"
    lg="ta"
elif audio_text in teg:
    vc="te-IN"
    lg="te"
elif audio_text in bbb:
    vc="hi-IN"
    lg="hi"
    d="bb"
else:
    print("sorry i didn't get it")

def respond(txt):
    out=translator.translate(txt, dest=lg)
    s=out.text
    r=s.split()
    if d=="bb":
        for i in r:
            if i in hibb:
                s=s.replace(i,braj[hibb.index(i)])   
    print(s)
    var=gTTS(text=s,lang=lg)
    var.save("op.mp3")
    playsound("op.mp3")
    os.remove("op.mp3")

def wish():
    respond("hello")
    time = int(datetime.datetime.now().hour)
    global uname,asname
    if time>= 0 and time<12:
        respond("Good Morning sir or madam!")
    elif time<18:
        respond("Good Afternoon sir or madam!")
    else:
        respond("Good Evening sir or madam!")
    #asname ="Jasper 1 point o"
    respond("I am your Voice Assistant ,")
    #respond(asname)
    print("I am your Voice Assistant,")

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=r.recognize_google(audio,language=vc)
            data="your request" + data
            respond(data)
            
        except sr.UnknownValueError:
            respond("Sorry I did not hear your question, Please repeat again.")
    if(d=="bb"):
        for i in data:
            if i in braj:
                data=data.replace(i,hibb[braj.index(i)])
    t=translator.translate(data, dest='en')
    return t.text

wish()
while(1):
    respond("How can I help you?")
    text=str(talk())
    print(text)
    try:
        if text==0:
            continue        
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break               
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        
        elif 'search'  in text:
            text = text.replace("search", "")
            text = text.replace(" ","")
            webbrowser.open_new_tab(text)
            #time.sleep(5)       
        elif 'google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)                     
        elif "open word" in text: 
            respond("Opening Microsoft Word") 
            os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk"') 
            respond("The answer is " + answer) 
        elif 'wikipedia' or 'who' or 'where' or 'which' or 'what' in text:
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
        elif 'play' or 'youtube' in text:
            song = text.replace('play','')
            respond('playing'+ song)
            pywhatkit.playonyt(song)  
        elif "calculate" or "what is" in text: 
            question=text
            app_id="R6H3XJ-6XYRJ4GV74"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = (res.results).text     
        else:
            respond("Application not available")
    except:
        respond("Sorry i did not get you")