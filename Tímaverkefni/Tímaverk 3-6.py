num = 10
cab = 0

while True:
    cab = num * num
    if cab % 100 == num:
        print(num)
        break
    num = num + 1
