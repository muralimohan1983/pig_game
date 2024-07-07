import computer

rollAgain = False
userPoints = 0
cpuPoints = 0
mode = input("what mode would you like 1 for computer 2 for multiplayer and q for quit").lower()

if mode == "q":
    print("you have exited the game")
    quit()
elif mode == "1":  # computer

    rollChoice = input("would like to roll first [y/n]").lower()

    if rollChoice == "y":
        rollAgain, userPoints = computer.player(userPoints)

    elif rollChoice == "n":
            rollAgain = False

    if rollAgain:
        computer.player(userPoints)

    elif not rollAgain:
        computer.cpu(cpuPoints)

elif mode == "2":  # multiplayer
    print("multiplayer")
