digits = int(input())

result = ""
arr = []

for i in range(3):
    row = list(map(int,input().split()))
    arr.append(row)

for i in arr:
    for j in i:
        if(j==7):
            result+="7"
            break
if(result == "777"):
    print(result)
else:
    print(0)
