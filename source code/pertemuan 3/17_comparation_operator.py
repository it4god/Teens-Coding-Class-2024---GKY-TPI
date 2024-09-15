# == compare equal
# != not equal 
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

username = input("Username : ")
password = input("Password : ")
if username != "along" or password != "123":
    print("Wrong credetials")
if username == "along" and password == "123":
    print("Login successful")
    