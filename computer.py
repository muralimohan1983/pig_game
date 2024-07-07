import random
import time

rollAgain = False


def player(uPoints):
    global rollAgain
    while True:
        rollChoice = input("y to roll n to give up chance to computer").lower()

        if rollChoice == "y":
            progressBar()
            diceNum = random.randint(1, 6)
            print(f"\r"  "You have rolled, your dice number is ", diceNum)

            if diceNum == 1:
                rollAgain = False
                print("You have rolled a 1 it's now the cpu's turn")
                break
            else:
                uPoints += diceNum
                print("your total points are", diceNum)
                continue

        elif rollChoice == "n":
            print("It's now the computers turn")
            rollAgain = False
            break

    return rollAgain, uPoints


def cpu(cPoints):
    global rollAgain
    print("Now it's my turn I am rolling dice"),

    progressBar()

    diceNum = random.randint(1, 6)
    print("\r" + "My number is ", diceNum)

    if diceNum == 1:
        print("oh no!!  I have rolled a one and my points have been reset it is your turn")
        rollAgain = False
        player()
    else:
        cpuDecission = random.randint(1, 2)

        if cpuDecission == 1:
            print(" I am rolling again\n\n")
            cPoints += diceNum
            rollAgain = True

        elif cpuDecission == 2:
            print("i don't want to roll again, It's your turn to roll")
            rollAgain = False

        return cPoints, rollAgain


def progressBar():
    for i in range(1, 3):
        print("-", end=" ", flush=True)
        time.sleep(0.5)

    print("\r", end=" ")

    time.sleep(0.5)

    for i in range(1, 7):
        print("-", end=" ", flush=True)
        time.sleep(0.5)

    print("\r", end=" ")
