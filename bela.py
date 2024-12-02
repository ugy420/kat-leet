inp = input().split()

hands = int(inp[0])
dom = inp[1]
arr = []
for _ in range(4*hands):
    card = input()
    arr.append(card)
pts = 0

for i in arr:
    if(i[1]==dom):
        if(i[0]=='A'):
            pts+=11
        elif(i[0]=='K'):
            pts+=4
        elif(i[0]=='Q'):
            pts+=3
        elif(i[0]=='J'):
            pts+=20
        elif(i[0]=='T'):
            pts+=10
        elif(i[0]=='9'):
            pts+=14
    else:
        if(i[0]=='A'):
            pts+=11
        elif(i[0]=='K'):
            pts+=4
        elif(i[0]=='Q'):
            pts+=3
        elif(i[0]=='J'):
            pts+=2
        elif(i[0]=='T'):
            pts+=10 
print(pts)