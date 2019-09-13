"""
Program: nicelist.py
Author: Carol Ann Killeen
Date: 9/10/19

This program will allow the user to add people's names to one of two text files. One for "nice" people and one for "naughty" people. The user can continue to add people until a STOP command is issued.
The files will use "append mode" so the program can always add new people in the future without removing the old people added.
"""

while True:
	# Accept the input
	status = input("Is this person NAUGHTY or NICE? Type STOP to quit >>> ")
	status = status.upper()

	if status == "STOP":
		break
	elif status == "NAUGHTY":
		myFile = open("bad_list.txt", 'a')
		name = input("Enter the naughty person's name >>> ")
		myFile.write(name + "\n")
		myFile.close()
	elif status == "NICE":
		myFile = open("nice_list.txt", 'a')
		name = input("Enter the nice person's name >>> ")
		myFile.write(name + "\n")
		myFile.close()
	else:
		print("Sorry, that's not one of the choices!!")

print("You better watch out ... ")