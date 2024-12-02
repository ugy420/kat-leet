moves = input()
cup = 1

for i in moves:
    if(i=='A'):
        if(cup==1):
            cup = 2
        elif(cup==2):
            cup = 1
    elif(i=='B'):
        if(cup==2):
            cup = 3
        elif(cup==3):
            cup = 2
    elif(i=='C'):
        if(cup==3):
            cup = 1
        elif(cup==1):
            cup = 3
print(cup)