class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase

    def display(self, confirmed_letters):
        display_list = []

        # Create a "Phrase string" for the user
        for letter in self.phrase:
            if letter == " ":  # Ignore spaces
                display_list.append(letter)
            elif letter.lower() in confirmed_letters:

                for used_letter in confirmed_letters:
                    if letter == used_letter.upper():#UpperCase
                        display_list.append(letter)
                    elif letter == used_letter.lower():#Lowercase
                        display_list.append(letter)

            else:
                display_list.append("_")

        # The bellow print might look like ____ ar_ _r_a_
        print("".join(display_list))


    def check_letter(self, letter):
        if letter.lower() in self.phrase: #To see if the letter is lowercase
            return True
        elif letter.upper() in self.phrase: #To see if the letter is uppercase
            return True
        return False


    def check_complete(self, confirmed_letters):
        # If a letter in self.phrase has not been guessed, return False
        for letter in self.phrase:
            if letter.lower() not in confirmed_letters and letter != " ": #this also ignore spaces
                return False
        return True