# and  -> harus semua nya benar -> benar
# or  -> salah satu benar -> benar 
# not

x = int(input("x : "))
y = int(input("y : "))

if x < 5 and y > 10:
    print("X < 5 and y > 10")

if x < 5 or y > 10:
    print("X < 5 or Y > 10")

if not(x < 5 and y > 10):
    print("When x >= 5 or y <= 10")

while not True:
    print("Ini ga akan di print")
    
while True and False:
    print("Ini ga akan di print")
    
while not True:
    print("Ini ga akan di print")

if not False:
    print("Ini akan di print")

if not True:
    print("Ini ga akan di print")
    
username = "limpingen"
password = "123"

if username == "limpingen" and password == "123":
    print("Login Sukses")
if username != "limpingen" or password != "123":
    print("Login Failed")