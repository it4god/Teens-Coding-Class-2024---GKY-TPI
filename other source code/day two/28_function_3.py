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
Y = int(input("Input Y :"))
Addition(X,Y)
Subtraction(X,Y)
Multiply(X,Y)
Divide(X,Y)


