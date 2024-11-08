import random

print("This is a number guessing game.You got 5 chances to guess the number.Let's start.")

num = random.randrange(100)

chances = 5

counter = 0

while counter < chances:

    counter += 1
    guess = int(input('Please Enter your Guess : '))

    if guess == num:
        print("The number is",num,"and you guessed it right")
       