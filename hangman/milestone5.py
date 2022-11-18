import random

class Hangman():
    
    def __init__ (self, word_list, num_lives=5):
        # list - a list of possible words
        self.word_list = word_list
        
        #int number of lives player has
        self.num_lives = num_lives
        
        #str - word to be guessed picked randomly from word list
        self.word = random.choice(self.word_list)
        
        #list - a list of letters of the word with _ for letters not guessed yet
        self.word_guessed = ["_" for i in self.word]
        
        #int - number of letters in word that have not been guessed yet
        self.num_letters = len(self.word)
        
        #list - a list of guesses already tried
        self.list_of_guesses = []
     
       
    def check_guess(self, guess):
        check = guess.lower()
        if check in self.word:
            print(f"Good guess! {guess} is in the word")
            
            index = 0
            for letter in self.word:
                if check == letter:
                    self.word_guessed[index] = check
                    self.num_letters -= 1
                index += 1
                    
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            
        self.list_of_guesses.append(guess)
            
            
    def ask_for_input(self):
        while True:
            print(self.word_guessed)
            print(f"There are {self.num_letters} letters left.")
            guess = input("please enter a letter: ")
            
            if not len(guess) == 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
              print("You already tried that letter!")  
                        
            else:
                self.check_guess(guess)
                break

#Milestone 5 code logic of the game
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        
        #Checks if lives are 0, prints lose message and breaks loop
        if game.num_lives == 0:
            print("You lost!")
            break
            
        #Continues if lives greater than 0    
        if game.num_letters > 0:
            game.ask_for_input()
            
        #lives are greater than 0 and letters remaining are 0 is win condition    
        else:
            print(f"Congratulations. You won the game! The word was {game.word}")
            break
        
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
 
