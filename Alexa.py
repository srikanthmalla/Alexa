import speech_recognition as sr
from modules.ytsearch import ytsearch

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Recording..")
    audio = r.listen(source)
txt=r.recognize_google(audio,language="en-US")
print('searching:',txt)
ytsearch(txt)
