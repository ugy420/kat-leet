str = input()
k = 0
b = 0

for i in str:
    if(i=='k'):
        k+=1
    elif(i=='b'):
        b+=1
if(k>b):
    print("kiki")
elif(b>k):
    print("boba")
elif(b==k):
    if(b==0 and k==0):
        print("none")
    else:
        print("boki")