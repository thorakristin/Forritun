m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(2,(n+1)and(m+1)):
    if n%i == 0 and m%i == 0:
        largest = i
print(largest)