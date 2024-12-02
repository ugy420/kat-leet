n, m = map(int, input().split())

arr = [0]*400

for i in range(1,1+n):
    for j in range(1,1+m):
        arr[i+j]+=1

maxVal = max(arr)

for i in range(len(arr)):
    if(arr[i]==maxVal):
        print(i)