import random
import re
import os


from phrase import Phrase

list_of_phrases = ["The boy cried wolf",
                   "Testing the waters",
                   "Better to have it and not need it than need it and not have it",
                   "A dog is a man best friend",
                   "Bad news travels fast",
                   "Better late than never",
                   "Dead men tell no tales",
                   "Do not bite the hand that feeds you"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Game:
	
	def __init__(self):
		self.phrases = [Phrase(phrase) for phrase in list_of_phrases]
		self.active_phrase = random.choice(self.phrases)

		self.confirmed_letters = []
		self.missed = 0
		self.Finished = False
		self.guessedL = ""


	def welcome(self):

		print("Welcome to the game Phrase Hunter!")
		print("----------------------------------")
		print("")
		print("This game is like Hangman. A random phrase will be output on the screen as underscroes." +
			"\nThe game will keep track of what you've entered. You have 5 guesses total, so be careful!")
		print("")
		continue_game = input("Press Enter to continue.")


	def start(self):

		checkL = ""
		self.welcome()
		
		while (self.missed != 5) and (self.Finished == False):#if 5 inputs are incorrect or finished, game ends.

			clear_screen()
			print("Letters that were Used: ")
			print(*self.confirmed_letters, sep = (", "))#displays the list of used letters
			self.guessedL = self.get_guess()
			
			#checks to see if the letter was used

			checkL =self.active_phrase.check_letter(self.guessedL)
			if checkL == False:
				self.confirmed_letters.append(self.guessedL.lower())	
				self.missed +=1

			else:
				self.confirmed_letters.append(self.guessedL.lower())

			self.Finished = self.active_phrase.check_complete(self.confirmed_letters)#Checking to see if the phrase is complete, returns a boolean

			if self.Finished == True:
				print("Letters that were Used: ")
				print(*self.confirmed_letters, sep = (", "))
				self.Winner()

		self.game_over() #if while loop ends, game over. player loses 

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


	def get_guess(self):#check to see if the guessed letter is good
		
		fixed = False
	
		print("Current playing board")
		print("Number of mistakes out of 5: {} ".format(self.missed))
		print("")
		self.active_phrase.display(self.confirmed_letters)
		print("")

		while (True):
			self.guessedLetter = input("Guess a letter for the Phrase on the board: ")

			if self.guessedLetter.lower() in self.confirmed_letters:
				print("You already typed that letter in. Type in a different letter.")
				guessedL = input(">> ")

			else:
				break

		while fixed != True: #Triggering the error means you've entered a letter. This is correct
		
			try:#Number check
				if int(self.guessedLetter) or self.guessedLetter == '0':
					print("Invaild character entry. Type in letters, try again.")
					self.guessedLetter = input(">> ")
			except:
				fixed = True
				#self.active_phrase.display(self.guessedLetter)

				#Checking for symbols
			if re.search(r'[^\w]', self.guessedLetter):
				print("Symbols shouldn't be entered. Type in letters, try again.")
				fixed = False
				self.guessedLetter = input(">> ")

			elif len(self.guessedLetter) > 1:
				print("There shouldn't be more than one characters entered. Type in letters, try again.")
				fixed = False
				self.guessedLetter = input(">> ")

		return self.guessedLetter


	def Winner(self): #If you guessed everything correctly and win
		clear_screen()
		print("")
		print("You've Won!")
		print("The number of mistakes left were: {}".format(self.missed))
		self.active_phrase.display(self.confirmed_letters)
		print("")


	def game_over(self):
		if self.missed == 5: #If 5 mistakes are reached, end the game.
			clear_screen()
			
			print("Letters that were Used: ")
			print(*self.confirmed_letters, sep = (", "))
			print("")
			print("You've Lost... You've made too many mistakes.")
			print("The phrase was '{}'".format(self.active_phrase.phrase))
			print("")

	
