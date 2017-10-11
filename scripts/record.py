import speech_recognition as sr
from modules.youtube import *
from modules.notifications import Notification
from scripts.respond import say
import re

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
def record_command():
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		txt=r.recognize_google(audio,language="en-US")
		print(txt)
		splitted = re.sub("[^\w]", " ",  txt).split()
		# print(splitted)
		command=splitted[0]
		# print(command)
		notification.recording(command)
		if command.lower() =='youtube':
			if (splitted[1].lower()=='music'):
				yt_link=ytsearch(splitted[2:None])
				p=musicplay(yt_link)
			else:
				yt_link=ytsearch(splitted[1:None])
				ytplay(yt_link)
				return False
	except sr.UnknownValueError:
		print('cannot understand what you said..')
		return True


