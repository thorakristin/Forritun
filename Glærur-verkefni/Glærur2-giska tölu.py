#get an initial guess
guess_str = input("Guess a number: ")
guess = int(guess_str) #convert string to a number

#while guess is range, keep asking
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed Too High.")
    elif guess < number:
        print("Guessed Too low.")
    else:
        print("You guessed it. The number was:",number)
        break

    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early, the number was:",number)
