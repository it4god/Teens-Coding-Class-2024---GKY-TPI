import random

player1 = random.randint(1,6)
player2 = random.randint(1,6)

if player1 > player2:
    print("Player 1 menang")
elif player2 > player1:
    print("Player 2 menang")
else:
    print("Seimbang")


