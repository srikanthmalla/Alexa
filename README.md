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

commands to say: youtube (anything video you want to search)

youtube music (anysong/music you want to play on back end)

## Dependencies

sudo apt-get install google-chrome (install adblock extension in chrome)

these modules are needed to install, just run (this will automatically install these) `./setup.sh`:

notify2, playsound, bs4, vlc, pafy, git+https://github.com/Khang-NT/youtube-dl.git

### TODO:

when playing music, that procedure taking memory not listening to alexa command. So, may be start parallel processes.
