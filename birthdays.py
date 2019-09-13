"""
Program: birthdays.py
Author: Carol Ann Killeen
Date: 9/11/19

Program will display a list of names. When the user types a valid name, that person's birthday will display. If the user does not enter a valid name, an error will be displayed and they can try again.
"""

# Dictonary object to store the names and associated birthdays
birthdays = {"Albert Einstein":"03/14/1879",
			 "Ben Franklin":"01/17/1706",
			 "Bill Gates":"10/28/1955",
			 "Plato":"424 BC",
			 "Guido Van Rossum":"01/31/1956"}

while True:
	print("welcome to the birthday directory. We can tell you the birthdays of:")
	print()
	# The for loop counter refers to the keys of the dictonary
	# The loop will print the names of the people only
	for name in birthdays:
		print(name)

	person = input("Which person do you want to know the birthday of? Type QUIT to exit >>> ")

	if person in birthdays:
		print() # Blank to add space
		print("The birthday for " + person + " is " + birthdays[person])
		print() # Blank to add space
	elif person.upper() = "QUIT":
		print("See Ya")
		break
	else:
		print() # Blank to add space
		print("Sorry, " + person + " is not in our database. Try again.")
		print("\n\n") # 2 \n to add 2 empty lines
