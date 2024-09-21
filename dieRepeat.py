import dieRoll

number = 6

while True:
    print(dieRoll.rollDie(number))
    roll_again = input("roll again? ").lower()
    if roll_again != "yes":
        break