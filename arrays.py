import dieRoll

endResult = 0
number = 6
yes = ["yes", "yea", "yeah", "aye", "yep", "of course", "definitely", "indeed", "ok", "okay", "why not", "do so", "do it", "alright"]

while True:
    result = dieRoll.rollDie(number)
    endResult += result
    print(result)
    dieRoll.checkNumberForWinner(result)
    rollAgain = input("want to roll again? ").lower()
    if rollAgain not in yes:
        print("you rolled a total of", endResult)
        break
