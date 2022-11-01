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
To be updated
