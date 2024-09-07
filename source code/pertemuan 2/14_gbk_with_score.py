import random
#1. Gunting 
#2. Batu
#3. Kertas
computer_score = 0
player_score = 0
computer = random.randint(1,3)
player = int(input("1. Gunting, 2. Batu, 3. Kertas. Choice : "))

if computer == player:
    print("Seimbang")
elif computer == 1 and player == 2:
    print("Player menang")
elif player == 1 and computer == 2:
    print("Komputer menang")
elif computer == 2 and player == 3:
    print("Player menang")
elif computer == 3 and player == 2:
    print("Komputer menang")
elif computer == 1 and player == 3:
    print("Komputer menang")
elif computer == 3 and player == 1:
    print("Player menang")