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