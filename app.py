#Davonte' Whitfield
#Python 3.7
#Tech Degree Project 3 Prase Hunter


from game import Game
from phrase import Phrase

if __name__ == "__main__":
	game_on = True
	while game_on == True:
		game_on = Game().start()