# B_R_R
# M_S_A_W



def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)



inp_val=int(input("How many numbers:  "))
i=1
while i<inp_val:
    fibValue=fibonacci(i)
    print(fibValue)
    i+=1
print("All Done")
