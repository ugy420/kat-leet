l = int(input())
d = int(input())
x = int(input())

for i in range(l,d):
    sum = 0
    curnum=i
    while(i>0):
        t = i
        sum+=t%10
        i = i//10
    if(sum==x):
        print(curnum)
        break
lastnum = 0
for i in range(l,d+1):
    sum = 0
    curnum=i
    while(i>0):
        t = i
        sum+=t%10
        i = i//10
    if(sum==x):
        lastnum=curnum
print(lastnum)