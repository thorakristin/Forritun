d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
sum_d = d1 + d2

if (d1 <= 0 or d1 > 6) or (d2 <= 0 or d2 > 6):
    print("Invalid input")
elif sum_d == 7 or sum_d == 11:
    print("Winner")
elif sum_d == 2 or sum_d == 3 or sum_d == 12:
    print("Loser")
else:
    print(d1 + d2)
    
    


# Fill in the missing code below
