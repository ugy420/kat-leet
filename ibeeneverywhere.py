n = int(input())
op = [0] * n

for _ in range(n):
    pls = int(input())
    arr = []
    count = 0
    for l in range(pls):
        ele = input()
        arr.append(ele)
        if arr.count(ele) > 1:
            count +=1
    op[_] = pls - count

for i in op:
    print(i)