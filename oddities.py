n = int(input())
k = [0]*n
for i in range(n):
    k[i] = int(input())
for i in k:
    print(str(i) + " is even") if (i%2==0) else print(str(i) + " is odd")