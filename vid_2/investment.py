# B_R_R
# M_S_A_W


# Have the user ask their investment amount and expected interest rate.
"""Each year the investment will increase by original investmen
plus compounded investment multiplied to interest reate"""
# Print out the investment in 10 years.

inves=float(input("How much is your investment: "))
# we convert to float and round the percentege rate by 2 digits
inter=float(input("What is the percentage of usuary: "))*.01

for i in range(10):
    inves=inves+(inves*inter)

print("The investment after 10 years will be {:.2f}".format(inves))
