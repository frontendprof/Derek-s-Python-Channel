# B_R_R
# M_S_A_W


# For a received of string, print out acronym only.

# My way:

yword=input("What is your words: ").upper()
yword=yword.split()

emList=''

for i in yword:
  emList+=i[0]
print(emList)


# Derek's way:

# yword=input("What is your words: ").upper()
# yword=yword.split()
#
# for i in yword:
#   print(i[0],end="")
# print()
