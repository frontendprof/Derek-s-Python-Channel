# B_R_R
#M_S_A_W

message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))
 
secret_message = ""
for char in message:
 
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        secret_message += chr(char_code)
 
    else:
        secret_message += char
 
print("Encrypted :", secret_message)
 

orig_message = ""
 
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code -= key
 
       
 
        orig_message += chr(char_code)
 
    else:
        orig_message += char
 
print("Decrypted :", orig_message)
 


