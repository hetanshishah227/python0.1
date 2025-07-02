while True:

    import random

    number = random.randint(1, 3)
    guess = int(input("Guess a number between 1 and 3: "))

    while guess != number:
        if guess < number:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        guess = int(input("Guess again: "))

    print("Congratulations! You guessed the number correctly.")