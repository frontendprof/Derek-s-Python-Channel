# B_R_R
# M_S_A_W


# Accept a string
# Encode the received string into unicodes
# And decipher the unicodes back to its original form


# Convention of assigning characters with unicodes
# A - Z     ---> 65-90
# a - z     ---> 97-122
# ord("A")  ---> 65
# chr(65)   ---> A



# Enter a string to encode in uppercase
givenStr=input('What is your word in mind(in uppercase please): ').upper()

# Print encoded unicodes
secretStr=''
normStr=''
for char in givenStr:
    secretStr+=str(ord(char))
print("The encrypted string is --->", secretStr)


# Cycle through each charcter code 2 at a time
for i in range(0,(len(secretStr)-1),2):
    charCode=secretStr[i]+secretStr[i+1]

    # Decipher the encrypted code
    normStr+=chr(int(charCode))

# Print original string
print(normStr)
