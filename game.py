import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Enter your guess (1–100): "))

    if guess == number:
        print("Correct! You guessed it!")
        break
    elif guess > number:
        print("Too high, try again!")
    else:
        print("Too low, try again!")