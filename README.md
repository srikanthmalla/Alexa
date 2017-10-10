# Alexa (Linux Voice Assistant)

## Install Speech Recognition module (this uses google speech api)

```
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio==0.2.11
sudo python setup.py install
cd examples
python audio_transcribe.py
```

## Start using the Voice Assistant

```
 python Alexa.py  
```
call Alexa. when it hears you, it will respond by saying yes.

commands to say: youtube (anything you want to search)

## Dependencies

(notify2) sudo pip install notify2

sudo apt-get install google-chrome (install adblock extension in chrome)

these are usually installed by default:

playsound, bs4 (module name: beautiful soup 4)
