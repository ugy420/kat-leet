import math as m 

def isPrime(n):
    if(n<=1):
        return False
    elif(n>1):
        for i in range(2,int(m.sqrt(n))+1):
            if(n%i==0):
                return False
    return True
        
n = int(input("Enter number: "))
print(f"{n} is a prime number " if isPrime(n) else f" {n} is not a prime number")