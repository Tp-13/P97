import random
number = random.randint(1,99)
chance = 0
while chance < 10:
    guess = int(input("Enter Your Guess: "))
    if guess == number:
        print("You Guessed It!")
        break
    elif guess < number:
        print("Close! Try a number greater than", guess)
    else:
        print("Close! Try a number smaller than", guess)
    chance += 1
if not chance < 5:
    print("You were close, here's the answer: ", number)