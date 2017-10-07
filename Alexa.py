import speech_recognition as sr
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Recording..")
    audio = r.listen(source)

print(r.recognize_google(audio,language="en-US"))
