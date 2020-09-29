import csv
import os
import add

work = True
script_path = "../scripts/scripts.csv"

def commandList():
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			print(f"{row[0].split(',')[0]} - {row[0].split(',')[1]}")

while work == True:
	command = input("")
	comm_list = command.split()
	if comm_list[0] == "exit":
		work = False
	if comm_list[0] == "add":
		add.addCommand(comm_list[1], comm_list[2])
	if comm_list[0] == "list":
		commandList()		

