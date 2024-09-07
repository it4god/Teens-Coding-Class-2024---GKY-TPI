#yang menang 10x menang !!!

#import library random
import random 
player = 0
computer = 0
print("Playing Games : Rock Paper Scissor")
print("1. Rock, 2.Paper, 3. Scissor")
playerchoice = int(input("Please choice :")) 
computerchoice = random.randint(1,3) 
while player < 10 and computer < 10:
    if playerchoice == computerchoice:
        print("Stalemate")
    elif playerchoice == 1 and computerchoice == 2:
        print("Computer win !")
        computer = computer + 1
    elif playerchoice == 2 and computerchoice == 1:
        print("Player win !")
        player = player + 1
    elif playerchoice == 1 and computerchoice == 3:
        print("Player win !")
        player = player + 1
    elif playerchoice == 3 and computerchoice == 1:
        print("Computer win !")
        computer = computer + 1
    elif playerchoice == 2 and computerchoice == 3:
        print("Computer win !")
        computer = computer + 1
    elif playerchoice == 3 and computerchoice == 2:
        print("Player win !")
        player = player + 1
if player == 10:
    print("Player who win the game")
elif computer == 10:
    print("Computer who win the game")