#define a word list
words = ['apple', 'pie', 'tiresome', 'vibrator', 'acknowledge']

#make a random choice
import random

word = random.choice(words)

#create a loop for guessing
guess = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char, end = ' ')
        
        else:
            print('_', end = ' ')
            failed += 1

    if failed == 0:
        print("\nYou Won!")

    guess1 = input("\nGuess a letter: ")
    guess += guess1

    if guess not in word:
        turns -= 1
        print(f"Wrong, You have {turns} turns left.")

        if turns == 0:
            print(f"You lost, The word was '{word}'.")


