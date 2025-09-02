n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = int(input())

for i in range(n-1,-1,-1):
    print(arr[i])