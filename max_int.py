# User puts in a number.
# If the number is positive, the user always  puts in another number.
# When the user puts in a negative number, 
# the highest postivie number he had already put in will print.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line