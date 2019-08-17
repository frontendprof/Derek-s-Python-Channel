# B_R_R
# M_S_A_W


# Guessing game in range of 10
# Throws an erro upon non digital character entry


secret_number=6

while True:
    try:
        guess=int(input("What is your guess: "))

        if guess==secret_number:
            print("You've got it.")
            break

        else:
            print('Try again')

    except NameError:
        print("You did not enter a number.")
