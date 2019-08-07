# B_R_R
# M_S_A_W


while True:
	us_inp=eval(input('How old are you: '))

	# If age is under 5, then wait to grow to Kindergarden

	if us_inp<5:
		print(""""Wait some time to turn to be 5 years old, so you can
			go to Kindergarden""")

	# If age is 5, then go to Kindergarden
	elif us_inp==5:
		print("Go to Kindergarden")



	# If age between 6-17, then go to 1-12 grades
	elif (us_inp>5) and (us_inp<=17):
		grade=us_inp-5
		print(f'You have to be on grade of {grade}')


	# If age is over 17, then go to College
	else:
		print('Go to College')
