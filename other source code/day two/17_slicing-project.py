text = input("Text :")
n = int(input("N :"))

total = (len(text) // n ) + 1

for i in range(total):
    print(text[i*n:i*n+n])
