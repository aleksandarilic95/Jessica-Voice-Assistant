import os
import csv

exists = True
script_path = "C://Users/aleks/Desktop/Python/Voice Assistant/scripts/scripts.csv"

def addCommand(command,script):
	global exists
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			if checkIfCommandExists(command) or checkIfScriptExists(script):
				pass
			else:
				exists = False
		file_read.close()
		if exists == False:
			with open(script_path, 'a', newline='') as file_append:
				file_a = csv.writer(file_append)
				file_a.writerow([f"{str(command)},{str(script)}"])
			file_append.close()
		else:
			print("Command and/or script already exists")
	csvPrettify()

def checkIfScriptExists(script):
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			if not row == [] and row[0].split(',')[1] == str(script):
				return True
		return False	
		file_read.close()

def checkIfCommandExists(command):
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			if not row == [] and row[0].split(',')[0] == str(command):
				return True
		return False	
		file_read.close()

def csvPrettify():
	list_new = []
	with open(script_path, 'r') as file_read:
		file_r = csv.reader(file_read)
		for row in file_r:
			if not row == []:
				list_new.append(row)
		file_read.close()

	with open(script_path, 'w', newline='') as file_write:
		file_w = csv.writer(file_write)
		file_w.writerows(list_new)
		file_write.close()




