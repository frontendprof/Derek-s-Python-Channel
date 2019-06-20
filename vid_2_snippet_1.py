# B_R_R
# M_S_A_W

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# Needs addition, which includes other parameters where you can prompt stumpts length and width.

# Here is the logic for drawing a pine tree:
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

tall=eval(input("What is the height of the tree?  "))
space=tall-1
star=1
stump=tall-1

while tall !=0:

  for i in range(space):
    print(" ", end="")
  
  for i in range(star):
    print("*", end="")

  print()

  space-=1
  star+=2
  tall-=1

for i in range(stump):
  print(" ", end="")
print('#')
