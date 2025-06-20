n = int(input())
bpm = []
abpm = []

for i in range(n):
    b,p = map(float,input().split())
    bpm.append(b*60/p)
    abpm.append(60/p)

for j,k in zip(bpm,abpm):
    print(f"{j-k} {j} {j+k}")