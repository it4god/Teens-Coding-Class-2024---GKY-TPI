firstname = input("Firstname : ")
lastname = input("Lastname : ")
fullname = firstname + " " + lastname
print("My Fullname : " + fullname)
age = int(input("Age : "))
print("My Age : " + str(age) + " years old")

#Why age is number ? not text ?

#you can compare number with number
if age < 12:
    print("You cannot watch this Movie. Not suitable for this age.")
else:
    print("You can watch this Movie")

