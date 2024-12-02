n = int(input())
arr = []
for i in range(n):
    inp = int(input())
    num = 1
    for j in range(1,inp+1):
        num=num*j
        bum = num%10
    arr.append(bum)
for _ in arr:
    print(_)