"""
Program: doctor.py
Author: Carol Ann Killeen
Date: 9/10/19

Conducts an interactive session of nondirective psychotherapy
"""

import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "Go on, go on")

qualifers = ("Why do you say that ", "You seem to think that ", "Can you explain why ", "Tell me more about ")

replacements = {"I":"you", "i":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "you":"I", "are":"am"}

history = []

def reply(sentence):
	"""Builds and returns a reply to the user's sentence."""
	probability = random.randint(1, 4)

	history.append(sentence) # adds the user input to the history list

	if probability == 1:
		return random.choice(hedges)
	elif probability == 2 and len(history) > 3:
		# Doctor is going back to an earlier topic
		return "Earlier you said that " + changePerson(random.choice(history))
	else:
		return random.choice(qualifers) + changePerson(sentence)

def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns"""
	words = sentence.split()
	replyWords = []

	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)

def main():
	"""Handles the interaction between patient and 'doctor'."""
	print("Good morning, I hope you are well today.")
	print("What can I do for you? Or type QUIT to leave the chat.")

	while True:
		sentence = input("\n>>> ")
		if sentence.upper() == "QUIT":
			print("Have a nice day! Your $10,000 bill will be in the mail shortly.")
			break
		print(reply(sentence))

# The entry point for program execution
main()