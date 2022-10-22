import random 

word_list = ["strawberry", "blueberry", "banana", "kiwi", "grape"]
word = random.choice(word_list)

#Task 1 Iteratively check if input is a valid guess
while True:
    guess = input("please enter a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

#Task 2 Check whether the guess is in the word
if guess in word:
    print(f"Good guess! {guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


