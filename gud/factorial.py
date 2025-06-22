def factorialussy(n):
    if n==1:
        return 1
    else:
        return n*factorialussy(n-1)

n = int(input())
print(factorialussy(n))