import random
word_list = ["strawberry", "blueberry", "banana", "kiwi", "grape"]

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
        
        #int - number of unique letters in word that have not been guessed yet
        self.num_letters = len(set(self.word))
        
        #list - a list of guesses already tried
        self.list_of_guesses = []
        
        
        
new_game = Hangman(word_list)
print(new_game.word)
print(new_game.word_guessed)
print(new_game.num_letters)