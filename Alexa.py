import speech_recognition as sr
from modules.youtube import ytsearch, ytplay
from modules.notifications import Notification
notification=Notification()
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    notification.recording('youtube')
    audio = r.listen(source)
txt=r.recognize_google(audio,language="en-US")
print('searching:',txt)
yt_link=ytsearch(txt)
print(yt_link)
ytplay(yt_link)
