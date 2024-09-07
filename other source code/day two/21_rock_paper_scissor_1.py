#import library random
import random 

print("Playing Games : Rock Paper Scissor")
print("1. Rock, 2.Paper, 3. Scissor")
playerchoice = int(input("Please choice :")) 
computerchoice = random.randint(1,3) 

if playerchoice == computerchoice:
    print("Stalemate")
elif playerchoice == 1 and computerchoice == 2:
    print("Computer win !")
elif playerchoice == 2 and computerchoice == 1:
    print("Player win !")
elif playerchoice == 1 and computerchoice == 3:
    print("Player win !")
elif playerchoice == 3 and computerchoice == 1:
    print("Computer win !")
elif playerchoice == 2 and computerchoice == 3:
    print("Computer win !")
elif playerchoice == 3 and computerchoice == 2:
    print("Player win !")
    