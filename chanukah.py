p = int(input())
arr = [0]*p
for i in range(p):
    _,arr[i] = map(int,input().split())

numb = 1
for i in arr:
    candles = 0
    for j in range(1,i+1):
        candles += j
    candles = candles + i
    print(f"{numb} {candles}")
    numb+=1