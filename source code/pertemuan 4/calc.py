def add(a,b):
    print(a, "+", b, "=", a+b)
def subtract(a,b):
    print(a, "-", b, "=", a-b)
def multiply(a,b):
    print(a, "*", b, "=", a*b)
def divide(a,b):
    if b == 0:
        print("Error : divide by zero")
    else:
        print(a, "/", b, "=", a/b)
 
a = int(input("A : "))
op = input("Operator : ")
b = int(input("B : "))

if op == "+":
    add(a,b)
elif op == "-":
    subtract(a,b)
elif op == "*":
    multiply(a,b)
elif op == "/":
    divide(a,b)