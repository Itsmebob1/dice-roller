import random

def rollDie(sides):
    return random.randint(1, sides)

attempts = int(input("how many attempts? "))

i = 0

while i < attempts:
    i =+ 1
    print(rollDie(6))