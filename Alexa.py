import speech_recognition as sr
from modules.youtube import ytsearch, ytplay

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Recording..")
    audio = r.listen(source)
txt=r.recognize_google(audio,language="en-US")
print('searching:',txt)
yt_link=ytsearch(txt)
print(yt_link)
ytplay(yt_link)
