# B_R_R
# M_S_A_W



"""
Coding Problem on Exception Handling:
We will use all object such as: try/except/else/finally

"""


with open("new_file.txt",'w')as wf:
    wf.write("In the name of GOD, most gracious and merciful\nPeace"
             "be upon our beloved prophet salutations\nThird line code\nSome new codebase is here")


try:
    myFile=open("new_file.txt", 'r')

except FileNotFoundError as ex:
    print("File is not found, Try again...")
    print(ex.args)

else:
    print("File:\n",myFile.read())
    myFile.close()

finally:
    print("Finished working with file")
