from gtts import gTTS
from datetime import datetime
import playsound
import os

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "voicetime.mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove("voicetime.mp3")

now = datetime.now()

current_time = now.strftime("Current time is %H o %M and %S seconds")
speak(current_time)