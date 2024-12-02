n = int(input())
linet = []
lineb = []

for i in range(n):
    ln1 = input()
    ln2 = input()
    linet.append(ln1)
    lineb.append(ln2)

for i,j in zip(linet,lineb):
    print(i)
    print(j)
    string = ""
    for k,l in zip(i,j):
        if(k==l):
            string+="."
        else:
            string+="*"
    print(string)
    print()