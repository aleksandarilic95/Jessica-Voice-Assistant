import csv
import os
import add

work = True
script_path = "C://Users/aleks/Desktop/Python/Voice Assistant/scripts/scripts.csv"

def commandList():
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			print(row)
		file_read.close()

while work == True:
	command = input("")
	comm_list = command.split()
	if comm_list[0] == "exit":
		work = False
	if comm_list[0] == "add":
		add.addCommand(comm_list[1], comm_list[2])
	if comm_list[0] == "list":
		commandList()		
