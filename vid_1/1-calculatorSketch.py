# B_R_R
# M_S_A_W

# ---------- CALCULATOR ----------
# Receive 2 numbers separated by an operator and show a result
# Sample
# Enter Calculation: 5 * 6
# 5 * 6 = 30
 

while True:
	
	# Store the user input of 2 numbers and an operator
	num1, operator, num2 = input('Enter Calculation: ').split()
	 
	# Convert strings into integers
	num1 = int(num1)
	num2 = int(num2)
	 
	# If, else if (elif) and else execute different code depending on a condition
	if operator == "+":
	    print("{} + {} = {}".format(num1, num2, num1+num2))
	 
	# If the 1st condition wasn't true check if this one is
	elif operator == "-":
	    print("{} - {} = {}".format(num1, num2, num1 - num2))
	elif operator == "*":
	    print("{} * {} = {}".format(num1, num2, num1 * num2))
	elif operator == "/":
	    print("{} / {} = {}".format(num1, num2, num1 / num2))
	 
	# If none of the above conditions were true then execute this by default
	else:
		print("Use either + - * or / next time")