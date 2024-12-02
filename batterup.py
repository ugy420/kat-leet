n = int(input())

pts = map(int,input().split())

div = 0
sum = 0

for i in pts:
    if(i>=0):
        div+=1
        sum+=i
print(sum/div)