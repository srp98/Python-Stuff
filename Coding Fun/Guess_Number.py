# Simple Guessing Game
# Import required Lib's
from random import randint

# Get Secret Number
secret_number = randint(1, 20)

# Ask user to take a guess 6 times
for i in range(6):
    print('Take a guess...')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break

if guess == secret_number:
    print(f'Good Job! You guessed my number in {i} guesses')
else:
    print(f'Nope. The number i was thinking of was {secret_number}')
