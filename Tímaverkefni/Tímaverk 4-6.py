top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1,(top_num+1)):
    perf_num = 0
    for j in range(1,i):
        if i % j == 0:
            perf_num = perf_num + j
    if perf_num == i:
        print(i)


    


    
  