# Alexa (Linux Voice Assistant)

## Install Speech Recognition module (this uses google speech api) and Alexa

```
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio==0.2.11
sudo python setup.py install
cd examples
python audio_transcribe.py
cd
git clone git@github.com:srikanthmalla/Alexa.git
cd Alexa
./setup.sh
```
ffmpeg  is also needed

## Start using the Voice Assistant

```
 python Alexa.py  
```
call Alexa. when it hears you, it will respond by saying yes.

commands to try: music californication (this will play the song on back end as parallel process)

## Dependencies

These modules are needed to install, just run `./setup.sh` (this will automatically install these):

notify2, playsound, bs4, vlc, pafy, git+https://github.com/Khang-NT/youtube-dl.git

## List of Module :

Youtube-Music (command: music ----)
Youtube-Video (command: video ----)

### TODO:

Add more modules and intelligence

