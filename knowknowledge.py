n = int(input())
lrn = input().split()
lrnt = input().split()

sum1,sum2 = 0,0
for i in lrn:
    sum1 += int(i)

for i in lrnt:
    sum2 += int(i)
print(sum1-sum2)
    