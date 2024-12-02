wspd = int(input())
n = int(input())

sta = [0]*n
sspd = [0]*n

for i in range(n):
    sta[i], sspd[i] = map(str, input().split())
    sspd[i] = int(sspd[i])

for i in range(n):
    print(sta[i] + " opin" ) if (sspd[i]>=wspd) else print(sta[i] + " lokud" )
