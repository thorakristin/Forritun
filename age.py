num = int(input("Enter your age: "))

if num >= 0 and num <=34:
    print("Young")
elif num >= 35 and num <= 50:
    print("Mature")
elif num >= 51 and num <= 69:
    print("Middle-aged")
elif num >= 70:
    print("Old")
else:
    print("Invalid age")