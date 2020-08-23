import random
import re


class Phrase:
	

	def __init__(self):
		#Multiple phrases are here for possible replayability of the game
		self.list_of_phrases = ["The boy cried wolf",
							 "Testing the waters",
							 "Better to have it and not have it than need it and not have it",
							 "A dog is a man best friend",
							 "Bad news travels fast",
							 "Better late than never",
							 "Dead men tell no tales",
							 "Do not bite the hand that feeds you"]
	

	def picking_phrase(self): #This method get a random number of the index within "list_of_phrases" to get one at random
		random_num = random.randint(1, len(self.list_of_phrases) - 1) 
		return self.list_of_phrases[random_num] #send it to game's _init_


	def display(uscorePhrase, phrase ):#For displaying
		#when the game start, variable must be 0
		i = 0 
		if any(uscorePhrase):#checking to see if empty, if not variable is 1 to skip to print
			i = 1

		if i == 0:
			uscorePhrase = ("_" * len(phrase))
			i+=1
			return uscorePhrase

		else:
			print(uscorePhrase) #The playing board


	def check_letter(guessedL, loop_count, confirmed_letters):#This method looks to see if the letter was used
		letter_check = False # Resetting variable

		while letter_check == False and loop_count >= 1:#checking to see if 'loop_count' is 0. if so, skip. first entry is ' '
			
			if guessedL not in confirmed_letters:
				confirmed_letters.append(guessedL.lower())
				letter_check = True

			else:
				print("You already typed that letter in. Type in a different letter.")
				guessedL = input(">> ")

		return guessedL, confirmed_letters#only returning letter and the list of used letters


	def check_complete(uscorePhrase):
		if re.search(r"_", uscorePhrase): return False #Cheaking to see if there are underscores in the playing board still.
		else: return True
			

