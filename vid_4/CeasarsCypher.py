# B_R_R
# M_S_A_W


message=input("Enter your message: ")

key =int(input("How many characters you want to shift: "))

secret_message =""

for char in message:

  if char.isalpha():
    char_code=ord(char)
    char_code+=key

    if char.isupper():


      if char_code>ord("Z"):
        char_code-=26

      elif char_code<ord("A"):
        char_code+=26

    else:
      if char_code>ord("z"):
        char_code-=26

      elif char_code<ord("a"):
        char_code+=26

    secret_message+=chr(char_code)

  else:
    secret_message+=char

print(secret_message)


key=-key
orig_message=""

for char in secret_message:

  if char.isalpha():
    char_code=ord(char)
    char_code+=key

    if char.isupper():


      if char_code>ord("Z"):
        char_code-=26

      elif char_code<ord("A"):
        char_code+=26

    else:
      if char_code>ord("z"):
        char_code-=26

      elif char_code<ord("a"):
        char_code+=26

    orig_message+=chr(char_code)

  else:
    orig_message+=char

print(orig_message)
