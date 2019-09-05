num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 >= num2 and num1 >= num3:
    max_int = num1
elif num2 >= num1 and num2 >= num3:
    max_int = num2
else:
    max_int = num3

print("The maximum is: ", max_int)
