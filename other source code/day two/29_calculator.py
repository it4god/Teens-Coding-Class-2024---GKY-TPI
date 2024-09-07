def Addition(X,Y):
    print(X, "+", Y, "=", X+Y)
def Subtraction(X,Y):
    print(X, "-", Y, "=", X-Y)
def Multiply(X,Y):
    print(X, "*", Y, "=", X*Y)
def Divide(X,Y):
    if Y == 0:
        print("Cannot Divide with 0")
    else:
        print(X, "/", Y, "=", X/Y)

X = int(input("Input X :"))
op = input("Operator : ")
Y = int(input("Input Y :"))
if op == "+":
    Addition(X,Y)
elif op == "-":
    Subtraction(X,Y)
elif op == "*":
    Multiply(X,Y)
elif op == "/":
    Divide(X,Y)