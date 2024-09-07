age = int(input("Age : "))
if age >= 0 and age <= 2:
    print("Baby")
elif age > 2 and age <= 5:
    print("Toddler")
elif age > 5 and age <= 11:
    print("Kids")
elif age > 11 and age <= 18:
    print("Teenagers")
elif age > 18 and age <= 21:
    print("Youth")
elif age > 21 and age <= 25:
    print("Young Adult")
elif age > 25 and age <= 45:
    print("Adult")
elif age > 45 and age <= 60:
    print("Middle Age")
elif age > 60 and age <= 80:
    print("Senior Age")
else:
    print("You have BONUS life from God")