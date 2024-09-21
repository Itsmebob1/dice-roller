import random

def rollDie(sides):
    return random.randint(1, sides)

number = int(input("how many sides do yu want to have? "))

print(rollDie(number))