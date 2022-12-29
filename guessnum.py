import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: " ))
        if guess > random_number:
            print("Sorry. Guess number is so high.Guess again ")
        elif guess < random_number:
            print("Sorry. Guess number is too low. Guess again ")

    print(f"Congrats! You guessed a number {random_number}")

guess(10)