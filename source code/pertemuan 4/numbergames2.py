import random
print("Welcome to Number game !")
print("Computer will generate a random and you must guess in max 5 times")

life = 5
result = random.randint(1,100)
guess = int(input("Guess the Number : "))
while life > 0:
    if result == guess:
        print("You win")
        break
    elif result < guess:
        if guess - result <= 3:
            print("Close Enough. Please guess lower number")
        else:
            print("Please guess lower number")
        life = life - 1
        guess = int(input("Guess the Number : "))
    elif result > guess:
        if result - guess <= 3:
            print("Close Enough. Please guess higher number")
        else:
            print("Please guess higher number")
        life = life - 1
        guess = int(input("Guess the Number : "))
if life == 0:
    print("You lose")