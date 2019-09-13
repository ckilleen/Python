"""
Program: luckySevens.py
Author: Carol Ann Killeen
Date: 9/13/19
"""

import random

while True:
	pot = int(input("Please enter the amount of money you wish to enter into the pot >>> "))
	diceroll1 = random.randint(1, 7)
	diceroll2 = random.randint(1, 7)
	roll = (diceroll1 + diceroll2)

	if roll == 7 and pot > 0:
		print()
		print("Your first roll is " + str(diceroll1) + ".")
		print("Your first roll is " + str(diceroll2) + ".")
		print("You won $4, your pot is $" + str(pot + 4) + " Play Again >>> ")
	elif pot > 0:
		print()
		print("Your first roll is " + str(diceroll1) + ".")
		print("Your first roll is " + str(diceroll2) + ".")
		print("You lost your money, your pot is $" + str(pot - 1) + " Play Again and loose more >>> ")
	else:
		print()
		print("Sorry, there's no more money in your pot. You lost it all! Have you learned your lesson yet?")
		print("Thank you for the money!")

print("Thanks for playing")