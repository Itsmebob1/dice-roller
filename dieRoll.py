import random

def rollDie(sides):
    return random.randint(1, sides)

def checkNumberForWinner(number):
    if number == 6:
        print("  /   /   /")
        print(" /   /   /   /  /---/")
        print("/___/___/   /  /   /")