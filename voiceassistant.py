import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import csv

speechnum = 1
work = True
repeat = False

script_path = "C://Users/aleks/Desktop/Python/Voice Assistant/scripts/scripts.csv"

def speak(text):
	global speechnum
	tts = gTTS(text=text, lang="en")
	filename = f"voice{speechnum}.mp3"
	speechnum += 1
	tts.save(filename)
	playsound.playsound(filename)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source, timeout = None,  phrase_time_limit = 4)
		said = ""

		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			pass

	return said

def delete_speech_files():
	global speechnum
	for i in range(1,speechnum):
		os.remove(f"voice{i}.mp3")
		speechnum = 1

def doCommand(command):
	found = False
	list_comm = command.split()
	newcommand = ""
	for item in list_comm:
		newcommand += str(item)
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			print(row)
			if row[0].split(',')[0] == str(newcommand):
				speak("Okay")
				found = True
				comm = row[0].split(',')[1]
				os.system(f"py scripts/{comm}.py")
		if found == False:
			speak("Sorry, command not found")
		file_read.close()


speak("hello")
while work == True:
	command = get_audio()
	if command.lower().startswith("jessica"):
		command2 = command.lower().split(' ', 1)[1]
		if command2 == "go to sleep":
			speak("I will miss you, goodbye")
			work = False
		if not command == "" and not command2 == "go to sleep":
			doCommand(command2)

	delete_speech_files()
			