# B_R_R
# M_S_A_W

def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
 
 
def getPrimes(numb):
 
    list_of_primes = []
 
    for a in range(2, numb):
 
        if isprime(a):
            list_of_primes.append(a)
 
    return list_of_primes
 
inp_num = int(input("Search for Primes up to : "))
 
b = getPrimes(inp_num)
 
for c in b:
    print(c)
