from bs4 import BeautifulSoup
import requests
import pprint
import playsound
from gtts import gTTS
import os
import scrapeyoutubechannels
import pprint

videos = []
all_videos = []

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove("voice.mp3")

for item in scrapeyoutubechannels.channel:
	found = False
	url= f"https://www.youtube.com/feeds/videos.xml?channel_id={item[1]}"
	html = requests.get(url)
	soup = BeautifulSoup(html.text, "lxml")
	name = item[0]
	last_video = item[2]

	for index, entry in enumerate(soup.find_all("entry")):
		help_list = ['h','h','h','h']
		if found == False:
			for title in entry.find_all("title"):
				help_list[0] = title.text
				if help_list[0] == last_video:
					found = True
			for link in entry.find_all("link"):
				help_list[1] = link["href"]
			for name in entry.find_all("name"):
				help_list[2] = name.text
			for pub in entry.find_all("published"):
				help_list[3] = pub.text
			videos.append(help_list)

	videos.pop(len(videos) - 1)
	all_videos.append(videos)
	videos = []

# pprint.pprint(all_videos)
	
channel_list = scrapeyoutubechannels.channel

for index, item in enumerate(all_videos):
	if(len(item[index]) == 0):
		speak(f"There are no new videos from user {channel_list[index][0]}")
	if(len(item[index]) == 1):
		speak(f"There is one new video from user {channel_list[index][0]}")
	else:
		speak(f"There are {len(item)} new videos from user {channel_list[index][0]}")

	for index, item in enumerate(item):
		speak(f"Video number {index+1}")
		speak(item[0])
