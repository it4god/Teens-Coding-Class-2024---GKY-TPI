import random
#1. Gunting 
#2. Batu
#3. Kertas
computer_score = 0
player_score = 0
computer = random.randint(1,3)
player = int(input("1. Gunting, 2. Batu, 3. Kertas. Choice : "))
while True:
    if computer == player:
        print("Seimbang")
        if computer == 1:
            print("Computer dan Player memilih Gunting")
        elif computer == 2:
            print("Computer dan Player memilih Batu")
        else:
            print("Computer dan Player memilih Kertas")
    elif computer == 1 and player == 2:
        print("Player menang")
        print("Player memilih Batu")
        print("Computer memilih Gunting")
        player_score += 1
    elif player == 1 and computer == 2:
        print("Komputer menang")
        print("Player memilih Gunting")
        print("Computer memilih Batu")
        computer_score += 1
    elif computer == 2 and player == 3:
        print("Player menang")
        print("Player memilih Kertas")
        print("Computer memilih Batu")
        player_score += 1
    elif computer == 3 and player == 2:
        print("Komputer menang")
        print("Player memilih Batu")
        print("Computer memilih Kertas")
        computer_score += 1
    elif computer == 1 and player == 3:
        print("Komputer menang")
        print("Player memilih Kertas")
        print("Computer memilih Gunting")
        computer_score += 1
    elif computer == 3 and player == 1:
        print("Player menang")
        print("Player memilih Gunting")
        print("Computer memilih Kertas")
        player_score += 1
    print("Player Score : " + str(player_score))
    print("Computer Score : " + str(computer_score))
    print("======================================================")
    computer = random.randint(1,3)
    player = int(input("1. Gunting, 2. Batu, 3. Kertas. Choice : "))
    if computer_score == 10:
        print("Computer win this game")
        break
    elif player_score == 10:
        print("Player win this game")
        break