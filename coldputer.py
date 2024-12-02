n = int(input())
daysMinusZero = 0

temp = map(int, input().split())

for i in temp:
    if i < 0:
        daysMinusZero += 1

print(daysMinusZero)