n = int(input("Input a natural number: ")) # Do not change this line

count = 2
prime = True

while n > count:
    if n % count == 0:
        prime = False
    count = count + 1

if prime:
    print("Prime")
else:
    print("Not prime")