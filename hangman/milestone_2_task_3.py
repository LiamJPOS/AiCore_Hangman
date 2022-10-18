guess = input("Please enter a letter: ")
print(guess)

if len(guess) == 1 and guess.isalpha():
    print("good guess")
else:
    print("Oops! That is not a valid input.")