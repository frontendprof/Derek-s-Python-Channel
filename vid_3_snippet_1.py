# B_R_R
# M_S_A_W

# This project prompt you for a input and encrypts it and then decrypts back.
# Uppercase, lowercase and white space are considered.

#A-Z 65-97
#a-z 97-122


norm_string = input("Enter a string to hide in uppercase: ")
 
secret_string = ""
 
# Cycle through each character in the string
for char in norm_string:
 
    # Store each character code in a new string
  secret_string += str(ord(char)+100)
 
print("Secret Message :", secret_string)
 
norm_string = ""
 
# Cycle through each character code 3 at a time by incrementing by
# Each time through since unicodes go from 65 to 90
for i in range(0, len(secret_string)-1, 3):
 
    # Get the 1st and 2nd and third for the 3 digit number
    char_code = secret_string[i] + secret_string[i+1]+secret_string[i+2]
 
    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code)-100)
 
print("Original Message :", norm_string)
