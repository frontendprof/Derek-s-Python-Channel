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

# Here is the logic for drawing a pine tree:
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

tall=eval(input("What is the height of the tree?  "))
white=tall-1
hashv=tall-white
stump=tall-1

while tall !=0:

  for i in range(white):
    print(" ", end="")
  
  for i in range(hashv):
    print("#", end="")

  print()

  white-=1
  hashv+=2
  tall-=1

for i in range(stump):
  print(" ", end="")
print('#')
