#!/usr/bin/env python3

import speech_recognition as sr
from scipy.io.wavfile import read
from os import path
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
(fs,w_file)=read("test.wav")#this is to do operations on that wav file
# use "test.wav" as the audio source
offset=28
duration=5
r = sr.Recognizer()
with sr.WavFile(WAV_FILE) as source:
    audio = r.record(source,duration,offset) # read the entire WAV file

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language="en-US"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
