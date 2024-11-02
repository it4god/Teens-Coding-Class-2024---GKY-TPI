colours = ['Red', 'Green', 'Yellow', 'Blue', 'Black', 'White']
print(colours)
print(colours[0])
print(colours[3])
print(colours[-1])
colours.append("Magenta")
print(colours[-1])
print(colours)
colours.remove("Red")
print(colours[0])
colours.clear()
print(colours)

if "Green" in colours:
    print("There is green")
if "Red" in colours:
    print("There is red")
else:
    print("There is no red")
    