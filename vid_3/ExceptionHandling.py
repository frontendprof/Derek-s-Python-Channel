# B_R_R
# M_S_A_W

# The User is asked to enter a number
# Whereby entry of non digit values prevented by exception handling


while True:
    try:
        number=int(input("Enter a number: "))
        break

    except NameError:
        print("You did not enter a number.")

    except:
        print("Unknown error ocurred")

print("Thank you for entering a number")
