# User inputs an integer
# a1=1, a2=2, a3=3, a4=6, a5=11, a6=20
# To find the next number in the row you have to add the 3 previous numbers together
# Doesn't work for the first three because there arent't three numbers before them to add

n = int(input("Enter the length of the sequence: ")) # Do not change this line
# we need to find the rule of the sequence
first_num = 1
second_num = 2
third_num = 3

for i in range(1,(n+1)):
    if i == 1:
        print(i)
        first_num = 1
    if i == 2:
        print(i)
        second_num = 2
    if i == 3:
        print(i)
        third_num = 3
    if i > 3:
        sum_num = first_num + second_num + third_num
        print(sum_num)
        first_num = second_num
        second_num = third_num
        third_num = sum_num