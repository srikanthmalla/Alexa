import speech_recognition as sr
from modules.notifications import Notification
from scripts.respond import say
from scripts.process_command import *
import re
from threading import Thread
from multiprocessing import Process
import time

notification=Notification()
r = sr.Recognizer()
def record_alexa():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        txt=r.recognize_google(audio,language="en-US")
        splitted = txt.split(' ', 1)
        print(splitted[0].lower())
        if (splitted[0].lower()=='alexa'): 
            say("yes")
            return True
        else: 
            return False
    except sr.UnknownValueError:
        return False
def error():
    print('cannot understand what you said..')

def record_command():
    done=False
    while (done==False):
        print('recording command')
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            txt=r.recognize_google(audio,language="en-US")
            done=True
        except sr.UnknownValueError:
            error()
            done=False
    print(txt)
    splitted = re.sub("[^\w]", " ",  txt).split()
    #notification.recording(splitted)
    if splitted[0].lower()=='stop':
        return splitted[1].lower(),'stop'
    else:
        process=process_command(splitted)
        if process is not 0:
            return splitted[0].lower(),process
        else: 
            return 0,0
