n,m = map(int,input().split())
secWord = ""

for i in range(n):
    line = input()
    for _ in line:
        if(_!='.'):
            secWord = secWord+_
print(secWord)