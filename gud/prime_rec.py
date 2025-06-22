import math

def isPrime(n,i):
    if n<2:
        return False
    if i==1:
        return True
    if n%i==0:
        return False
    return isPrime(n,i-1)

n = int(input())
print(int(math.sqrt(n)))
print(isPrime(n,int(math.sqrt(n))))