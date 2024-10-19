import random
print("Welcome to the Computer Number Games")

life = 7

#simpan angka di dalam hati

print("Now put the number in your heart and Computer will guess it")
print("You must be honest !")
result = 23
computerguessnumber = random.randint(1,100) #30

while True:
    tempcomputerguessnumber = computerguessnumber
    print(computerguessnumber, " is My Guess Number. Is that right number ?")
    print("1. The number is too high")
    print("2. Close enough. But the number is still too high")
    print("3. The number is too low")
    print("4. Close enough. But the number is still too low")
    print("5. That exact number !") 
    answer = int(input("Your Response : "))
    if answer == 1: #the number is too high
        print("The number is too high")
        life = life - 1
        computerguessnumber = computerguessnumber -  random.randint(5,25)
    elif answer == 2:
        print("Close enough. But the number is still too high")
        computerguessnumber = computerguessnumber -  random.randint(1,3)
        life = life - 1
    elif answer == 3:
        print("The number is too low")
        computerguessnumber = computerguessnumber +  random.randint(5,25)
        life = life - 1
    elif answer == 4:
        print("Close enough. But the number is still too low")
        computerguessnumber = computerguessnumber +  random.randint(1,3)
        life = life -1
    elif answer == 5:
        print("You win ! My Number is ", computerguessnumber)
        break
    if life == 0:
        print("You lose !")
        break
    
    
    