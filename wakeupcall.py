n,m = map(int, input().split())
bt = list(map(int, input().split()))
btn = list(map(int, input().split()))
su1 = 0
su2 = 0

for i,j in zip(bt,btn):
    su1 += i
    su2 += j

if(su1>su2):
    print("Button 1")
elif(su1<su2):
    print("Button 2")
else:
    print("Oh no")
