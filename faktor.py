import math

art, imp = map(int,input().split())

i=0
while imp>math.ceil(i/art):
    i+=1
print(i)