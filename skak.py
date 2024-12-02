pr, pc = map(int,input().split())
gr, gc = map(int,input().split())

moves = 0
if(pr != gr):
    moves+=1
if(pc != gc):
    moves+=1
print(moves)