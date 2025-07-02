import random
number = random.randint(1, 50)
starting=1
ending=50
c=0
guess=0
while guess != number:
    c=c+1
    print(f"your {starting} and {ending}")#f is format
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < number:
        print("Too low, try again.")
        starting=guess
    elif guess > number:
        print("Too high, try again.")
        ending=guess
    else:
        print(f"Congratulations! You guessed the number correctly.{c} tried")