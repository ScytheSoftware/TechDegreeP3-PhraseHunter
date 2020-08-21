import random
import re
import os


from phrase import Phrase

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")#check complete


class Game:
	

	def __init__(self):
		self.game_phrases = ""
		self.missed = 0
		self.uscorePhrase = ""
		#--------
		self.Finished = False
		self.loop_count = 0
		self.confirmed_letters = []
		self.checkerCounter = 0

	def get_active_phrase(self): #This method is receiving and setting the playing phrase. Also setting up play board for Phrase
		self.game_phrases = Phrase().send_phrases()
		random_num = random.randint(1, len(self.game_phrases) - 1) 
		self.game_phrases = self.game_phrases[random_num]
		self.uscorePhrase = ("_" * len(self.game_phrases))

	def welcome(self):
		print("Welcome to the game Phrase Hunter!")
		print("")
		print("This game is like Hangman. A random phrase will be output on the screen as underscroes." +
			"\nThe game will keep track of what you've entered. You have 5 guesses total, so be careful!")
		print("")
		continue_game = input("Press Enter to continue.")

	def auto_space(self):
		return " "

	def start(self):
		self.welcome()
		self.get_active_phrase()

		while (self.missed != 5) and (self.Finished == False):
			if " " in self.game_phrases and self.loop_count == 0:
				guessedL = self.auto_space()

			else:
				clear_screen()
				print("Letters that were Used: ")
				print(*self.confirmed_letters, sep = (", "))
				guessedL = self.get_guess()
				
			letter_check = False # Resetting variable

			while letter_check == False and self.loop_count >= 1:
				if guessedL not in self.confirmed_letters:
					self.confirmed_letters.append(guessedL.lower())
					letter_check = True

				else:
					print("You already typed that letter in. Type in a different letter.")
					guessedL = self.fix_guess()

			for letter in range(len(self.game_phrases)):
				if guessedL.lower() == (self.game_phrases[letter]).lower():

					temp = list(self.uscorePhrase)#These three line makes the word an array of chars to change the correct item out. 
			
					for i in range(len(self.game_phrases)):
						if guessedL.lower() == (self.game_phrases[i]).lower(): #If a word has two of the same letters, replace both
							if guessedL.upper() == self.game_phrases[i]:#UpperCase
								temp[i] = guessedL.upper()

							elif guessedL.lower() == self.game_phrases[i]:#Lowercase
								temp[i] = guessedL.lower()

					self.uscorePhrase = ''.join(temp) #Joins them in finished.

					self.checkerCounter = 0 #This resets to 0 if you entered a correct letter. 
					break

				else:
					self.checkerCounter += 1

			self.checkerCounter, self.missed = Phrase.check_letter(self.checkerCounter, self.missed)#Hanldes incorrect letter.
			
			self.Finished = Phrase.check_complete(self.uscorePhrase, self.Finished)#Checking to see if word is complete

			if self.Finished == True:
				print("Letters that were Used: ")
				print(*self.confirmed_letters, sep = (", "))
				self.Winner()


			self.loop_count += 1

		self.game_over()

		print("")
		print("Press [1] to reset Game")
		print("Press [2] to Quit")
		play_respone = input(">> ")

		fixed = False #Resetting fixed

		while fixed != True:
			if play_respone == "1" or play_respone == "2":
				fixed = True

			else:
				print("Invaild entry. The options are [1] or [2]. Try again")
				play_respone = input(">> ")

		if play_respone == "1":				
			return True

		elif play_respone == "2":
			return False

	def get_guess(self):
		
		fixed = False
	
		print("Current playing board")
		print("Number of mistakes out of 5: {} ".format(self.missed))
		Phrase.display(self.uscorePhrase) #The playing board
		print("\n")

		guessedLetter = input("Guess a letter for the Phrase on the board: ")

		while fixed != True: #Triggering the error means you've entered a letter, correct
		
			try:#Number check
				if int(guessedLetter):
					print("Invaild character entry. Type in letters, try again.")
					guessedLetter = input(">> ")
			except:
				fixed = True

				#Checking for symbols
			if re.search(r'[^\w]', guessedLetter):
				print("Symbols shouldn't be entered. Type in letters, try again.")
				fixed = False
				guessedLetter = input(">> ")

			elif len(guessedLetter) > 1:
				print("There shouldn't be more than one characters entered. Type in letters, try again.")
				fixed = False
				guessedLetter = input(">> ")

		return guessedLetter

	def fix_guess(guessedLetter):
		guessedLetter = input("Guess a letter for the Phrase on the board: ")

		return guessedLetter

	

	def Winner(self): #If you guessed evrything correct
		clear_screen()
		print("")
		print("You've Won!")
		print("The number of mistakes left were: {}".format(self.missed))
		Phrase.display(self.uscorePhrase)
		print("")

	def game_over(self):
		if self.missed == 5: #If 10 mistakes are reached, end the game.
			clear_screen()

			print("Letters that were Used: ")
			print(*self.confirmed_letters, sep = (", "))
			print("")
			print("You've Lose... You've made too many mistakes.")
			print("The phrase was '{}'".format(self.game_phrases))
			print("")

	