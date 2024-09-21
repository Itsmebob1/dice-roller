import dieRoll

number = 6
yes = ["yes", "yea", "yeah", "aye", "yep", "of course", "definitly", "indeed", "ok", "okay", "why not", "do so", "do it", "alright"]

while True:
    result = dieRoll.rollDie(number)
    print(result)
    dieRoll.checkNumberForWinner(result)
    rollAgain = input("want to roll again? ").lower()
    if rollAgain not in yes:
        break