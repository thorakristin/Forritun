i = 1
while i <= 18:
    par = int(input("Par of hole "+ str(i) +": "))
    score = int(input("Score on hole "+str(i)+": "))
    results = par - score
    i = i + 1

    if results == 0:
        print("par")
    elif results == 1:
        print("birdie")
    elif results == 2:
        print("eagle")
    elif results == 3:
        print("albatross")
    elif results > 3:
        print("invalid score")
    elif results == -1:
        print("bogey")
    elif results == -2:
        print("double bogey")
    elif results == -3:
        print("triple bogey")
    else:
        print("bad hole")