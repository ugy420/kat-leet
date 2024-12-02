n,x = map(int,input().split())

for i in range(n):
    cons = int(input())
    x-=cons

print("Jebb") if x>=0 else print("Neibb")