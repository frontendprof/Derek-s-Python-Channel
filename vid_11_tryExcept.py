# B_R_R
# M_S_A_W



"""
Coding Problem on Exception Handling:
How to raise Error
Using try and except
"""


class DogNameError(Exception):
    def __init__(self, *args,**kwargs):
        Exception.__init__(self, *args,**kwargs)


try:
    user_input=input("What is your dog name: ")
    if any(i.isdigit()for i in user_input):
        raise DogNameError

except DogNameError:
    print("Dog name can not take any number in it, Sorry.")
