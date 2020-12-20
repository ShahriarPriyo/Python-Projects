import random


def guess(x):
    random_number=random.randint(1,x)
    guess=0

    while guess != random_number:
        guess=int(input(f"Enter the number between 1 and {x}: "))

        if (guess>random_number):
            print("sorry,guess is too high")
        elif(guess<random_number):
            print("Sorry,guess is too low")
    print(f"congrats, you have guess right! 88{random_number}")

guess(10)
