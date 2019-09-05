num = int(input("Enter an integer: "))
sum = 0
largest_num = num
even_num = 0
odd_num = 0

while num > 0:
    sum = sum + num
    print("Cumulative total:", sum)

    if largest_num < num:
        largest_num = num
    
    if num % 2 == 0:
        even_num = even_num + 1
    else:
        odd_num = odd_num + 1

    num = int(input("Enter an integer: "))

if even_num !=0 or odd_num != 0:
    print("Largest number: ", largest_num)
    print("Count of even numbers: ", even_num)
    print("Count of odd numbers: ", odd_num)