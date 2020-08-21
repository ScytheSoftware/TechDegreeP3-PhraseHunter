
import re

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")#check complete


class Phrase:
	
	def __init__(self):
		self.game_phrases = ["The boy cried wolf",
							 "Testing the waters",
							 "Better to have it and not have it than need it and not have it",
							 "A dog is a man best friend",
							 "Bad news travels fast",
							 "Better late than never",
							 "Dead men tell no tales",
							 "Do not bite the hand that feeds you"]
		
	def send_phrases(self):
		return self.game_phrases

	def display(uscorePhrase):
		print(uscorePhrase) #The playing board

	def check_letter(checkerCounter, missed):
		if checkerCounter >= 1: #If entered a incorrect letter. Phrase will handle the values
			missed += 1
			checkerCounter = 0

		return (checkerCounter, missed)


	def check_complete(uscorePhrase, Finished):
		if re.search(r"_", uscorePhrase): Finished = False #Cheaking to see if there are underscores in the playing board still.
		else: Finished = True
		return Finished

	
			

