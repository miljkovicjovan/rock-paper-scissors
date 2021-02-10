import random 
import os

def playAgain():
    while True:
        choice = input("Do you want to play again? (y/n)").upper()
        if choice == "Y":
            os.system('cls')
            userInput()
            break
        elif choice == "N":
            os.system('cls')
            exit()
        else:
            os.system('cls')
            print("Wrong input, try again.")

def check(x):
    number = random.randint(1,3)
    if number == 1:
        move = "ROCK"
    elif number == 2:
        move = "PAPER"
    else:
        move = "SCISSORS"
    
    if move == x:
        os.system('cls')
        print("You and the computer chose the same so it's a TIE!")
        playAgain()
    else:
        if x == "ROCK":
            if number == 2:
                os.system('cls')
                print("Computer chose paper so you LOSE!")
                playAgain()
            elif number == 3:
                os.system('cls')
                print("Computer chose scissors so you WIN!")
                playAgain()
        elif x == "PAPER":
            if number == 1:
                os.system('cls')
                print("Computer chose rock so you WIN!")
                playAgain()
            elif number == 3:
                os.system('cls')
                print("Computer chose scissors so you LOSE")
                playAgain()
        else:
            if number == 1:
                os.system('cls')
                print("Computer chose rock so you LOSE!")
                playAgain()
            elif number == 2:
                os.system('cls')
                print("Computer chose paper so you WIN!")
                playAgain()  

def userInput():
    while True:
        move = input("rock, paper or scissors? ").upper()
        if (move != "ROCK" and move != "PAPER" and move != "SCISSORS"):
            os.system('cls')
            print("Wrong input, try again.")
            continue
        else:
            check(move)
            break

userInput()