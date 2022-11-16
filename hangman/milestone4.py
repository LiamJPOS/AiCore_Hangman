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
       
    def check_guess(self, guess):
        check = guess.lower()
        if check in self.word:
            print(f"Good guess! {guess} is in the word")
            
            index = 0
            times_appeared = 0
            for letter in self.word:
                if check == letter:
                    self.word_guessed[index] = check
                    times_appeared += 1
                index += 1
            self.num_letters -= times_appeared
                    
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            
    def ask_for_input(self):
        while True:
            guess = input("please enter a letter: ")
            
            if not len(guess) == 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
              print("You already tried that letter!")  
                        
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                
                print(self.word_guessed)
                print(f"There are {self.num_letters} unique letters left.")

         
new_game = Hangman(word_list)
print(new_game.word)
print(new_game.word_guessed)
print(new_game.num_letters)

if __name__ == '__main__':
    #word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    new_game.ask_for_input()