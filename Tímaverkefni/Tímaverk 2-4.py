grade = float(input("Input a grade: "))
grade == 0.0

if grade <= 5.0 and grade >= 0.0:
    print("Failing grade!")
elif grade >= 5.0 and grade <= 10.0:
    print("Passing grade!")
else:
    print("Invalid grade!")
