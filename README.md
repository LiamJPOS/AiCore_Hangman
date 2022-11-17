# AiCore Hangman
A project to consolidate knowledge of Python and related technologies by creating a hangman game.

## Milestone 1
Milestone 1 set up the dev environment for getting started. 
- Learning git and Github
- reviewing Python commands
- reviewing bash terminal
- reviewing markdown

## Milestone 2
Variables that will be used in the game were created. 

- A list of possible words the game generates was created.

```python
word_list = ["strawberry", "blueberry", "banana", "kiwi", "grape"]
```
- To set the word for each game, the random module was used.

```python
import random
word = random.choice(word_list)
```

- A variable was created to capture the user's guessed letter and error check the input.

```python 
guess = input("Please enter a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("good guess")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3
- Functions created to check if guessed letter is in randomly generated word
- Iterative error checking used when asking for input and further error checking done by keeping guesses lower case

```python
def check_guess(guess):
    check = guess.lower()
    if check in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("please enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()
```
## Milestone 4
- Hangman class set up and functions in milestone 3 moved as methods in class. 
- Class initialises variables needed for each instance of a new game. 
    - The word list 
    - Number of lives 
    - Word selected using random module from list of words 
    - A list to track user's letters guessed 
    - Number of unique letters in word remaining 
    - List to reveal correctly guessed letters position in unguessed word

```python
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
```
- Updated method that checks user's guess to define what happens if a letter is or isn't in the word

```python
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
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            
        self.list_of_guesses.append(guess)
            
            
    def ask_for_input(self):
        while True:
            guess = input("please enter a letter: ")
            
            if not len(guess) == 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.list_of_guesses:
              print("You already tried that letter!")  
                        
            else:
                self.check_guess(guess)
```

