years = int(input("Years: "))
people = float(307357870)
birth = float((years*365*24*60*60)/7)
death = float((years*365*24*60*60)/13)
immigrant = float((years*365*24*60*60)/35)
population = int(people + birth - death + immigrant)

if years >= 0:
    print("New population after", years, "years is", population)
else:
    print("Invalid input!")
