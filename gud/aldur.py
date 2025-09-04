n = int(input())
ages = [int(input()) for _ in range(n)]

young = ages[0] 

for i in ages:
    if i < young:
        young = i

print(young)
