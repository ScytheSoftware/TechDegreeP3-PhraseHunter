import re
import os


from phrase import Phrase

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")#check complete


class Game:
	

	def __init__(self):

		self.active_phrase = Phrase().picking_phrase()#receving one phrase to use for the game
		self.loop_count = 0
		self.missed = 0#To count incorrect letters
		self.confirmed_letters = [] #A empty list for the letters to go
		self.Finished = False
		self.checkerCounter = 0#A the loop that checks each letter
		self.uscorePhrase = ''
		

	def welcome(self):

		print("Welcome to the game Phrase Hunter!")
		print("----------------------------------")
		print("")
		print("This game is like Hangman. A random phrase will be output on the screen as underscroes." +
			"\nThe game will keep track of what you've entered. You have 5 guesses total, so be careful!")
		print("")

		continue_game = input("Press Enter to continue.")


	def auto_space(self):#the game will run once with the guess ' ' automatically 
		return " "


	def start(self):
		self.welcome()
		self.uscorePhrase = Phrase.display(self.uscorePhrase, self.active_phrase)#The only time this method will return anything
		
		while (self.missed != 5) and (self.Finished == False):#if 5 inputs are incorrect or finished, game ends.
			if " " in self.active_phrase and self.loop_count == 0:#runs once
				guessedL = self.auto_space()

			else:
				clear_screen()
				print("Letters that were Used: ")
				print(*self.confirmed_letters, sep = (", "))#displays the list of used letters
				guessedL = self.get_guess()
				
			#checks to see if the letter was used
			guessedL, self.confirmed_letters = Phrase.check_letter(guessedL, self.loop_count, self.confirmed_letters)

			#checks each letter loop
			for letter in range(len(self.active_phrase)):
				if guessedL.lower() == (self.active_phrase[letter]).lower(): #if guessed letter and board letter are the same while lower, then run if

					temp = list(self.uscorePhrase)#Takes the underscore display and make it a list in temp
			
					for i in range(len(self.active_phrase)):#begin to enter the letter(s) to play board
					
						if guessedL.upper() == self.active_phrase[i]:#UpperCase: Only 'upper' on guessed letter to see if it's the same
							temp[i] = guessedL.upper()#if so, add it

						elif guessedL.lower() == self.active_phrase[i]:#Lowercase: Only 'lower' of guessed letter to see if it's the same
							temp[i] = guessedL.lower()#if so, add it

					self.uscorePhrase = ''.join(temp) #Joins them into one string again. This changes play board
					Phrase.display(self.uscorePhrase, self.active_phrase)

					self.checkerCounter = 0 #This resets to 0 if you entered a correct letter. 
					break#break out the loop to start again

				else:
					self.checkerCounter += 1


			if self.checkerCounter >= 1: #If entered a incorrect letter, 'CheckerCounter' will be more then 1
				self.missed += 1 #adds to the incorrect count
				self.checkerCounter = 0#resets

			self.Finished = Phrase.check_complete(self.uscorePhrase)#Checking to see if the phrase is complete, returns a boolean

			if self.Finished == True:
				print("Letters that were Used: ")
				print(*self.confirmed_letters, sep = (", "))
				self.Winner()


			self.loop_count += 1 #if game isn't over, loop again. Mainly here to avoid 'auto_space'

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
		Phrase.display(self.uscorePhrase, self.active_phrase) #The playing board
		print("\n")

		guessedLetter = input("Guess a letter for the Phrase on the board: ")

		while fixed != True: #Triggering the error means you've entered a letter. This is correct
		
			try:#Number check
				if int(guessedLetter) or guessedLetter == '0':
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


	def Winner(self): #If you guessed everything correctly and win
		clear_screen()
		print("")
		print("You've Won!")
		print("The number of mistakes left were: {}".format(self.missed))
		Phrase.display(self.uscorePhrase, self.active_phrase)
		print("")


	def game_over(self):
		if self.missed == 5: #If 5 mistakes are reached, end the game.
			clear_screen()

			print("Letters that were Used: ")
			print(*self.confirmed_letters, sep = (", "))
			print("")
			print("You've Lose... You've made too many mistakes.")
			print("The phrase was '{}'".format(self.active_phrase))
			print("")

	