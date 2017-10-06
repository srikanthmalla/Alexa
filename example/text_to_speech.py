import requests

text="Hola ho"
url="https://translate.googleapis.com/translate_tts?q="+text+"&tl=es&client=gtx"

r=requests.get(url)

file_="tts_out.mpeg"
if r.status_code == 200:
    with open(file_, 'wb') as f:
        f.write(r.content)

from playsound import playsound
playsound(file_)
