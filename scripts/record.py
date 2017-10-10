import speech_recognition as sr
from modules.youtube import ytsearch, ytplay
from modules.notifications import Notification
from scripts.respond import say

notification=Notification()
r = sr.Recognizer()
def record_alexa():
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		txt=r.recognize_google(audio,language="en-US")
		splitted = txt.split()
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
		splitted = txt.split()
		command=splitted[0]
		print(command)
		notification.recording(command)
		if command.lower()=='youtube':
			yt_link=ytsearch(splitted[1:None])
			ytplay(yt_link)
			return False
	except sr.UnknownValueError:
		print('cannot understand what you said..')
		return True


