username = input("Username : ")
password = input("Password : ")

if username == "renaldo" and password == "123":
    print("Login successful")
else:
    print("Login failed")

#OR ( Another way )

if username == "renaldo":
    if password == "123":
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Login failed")

