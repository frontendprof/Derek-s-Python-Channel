# B_R_R
# M_S_A_W


# The height of pine tree corresponds to the same amount of space minus 1
# The amount of spaces + one equals the height
"""
     *
    ***
   *****
  *******
 *********
     #
"""
height = eval(input("How tall is the tree : "))


spaces = height - 1
stars = 1
stump = height - 1


while height != 0:


    for i in range(spaces):
        print(' ', end="")


    for i in range(stars):
        print('*', end="")

    print()

    spaces -= 1
    stars += 2
    height -= 1

for i in range(stump):
    print(' ', end="")

print("#")
