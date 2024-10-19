import random
print("Welcome to Number game !")
print("Computer will generate a random and you must guess in max 7 times")

life = 5
result = random.randint(1,100)
guess = int(input("Guess the Number : "))
while life > 1:
    if result == guess:
        print("You win")
        break
    elif result < guess:
        print("Please guess lower number")
        life = life - 1
        guess = int(input("Guess the Number : "))
    elif result > guess:
        print("Please guess higher number")
        life = life - 1
        guess = int(input("Guess the Number : "))
    if life == 0:
        print("You lose")