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

count = 0
for item in all_videos:
	for _ in item:
		count += 1

if count == 0:
	speak(f"There are no new videos")
if count == 1:
	speak(f"There is one new video")
	speak("Giving you the list now")
else:
	speak(f"There are {count} new videos")
	speak("Giving you the list now")



for index, item in enumerate(all_videos):
	print("=========================")
	print(channel_list[index][0])
	print("=========================")
	for item2 in item:
		print(item2[0])
		print(item2[1])
		dates = item2[3].split('T')
		times = dates[1].split('+')
		print(f"{dates[0]} {times[0]}")
		print("----------------------")
	scrapeyoutubechannels.updateChannel(index, item[0][0])


