n = int(input())

arr = [0]*n
count = 0

for i in range(0,n):
    arr[i] = int(input())
    if arr[i]%2!=0:
        count+=1
print(count)