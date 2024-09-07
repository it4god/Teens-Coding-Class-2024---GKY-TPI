gpa = float(input("GPA :"))
if 2.0 <= gpa < 2.4:
    print("Pass")
elif 2.4 <= gpa < 2.8:
    print("Good")
elif 2.8 <= gpa < 3.4:
    print("Very Good")
elif 3.4 <= gpa < 4.0:
    print("Excellent")
else:
    print("Failed")