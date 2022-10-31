import random 

word_list = ["strawberry", "blueberry", "banana", "kiwi", "grape"]
word = random.choice(word_list)

#Task 3 Create functions to run the code checks
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