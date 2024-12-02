n = input()
a = int(input())
b = int(input())
a_b = int(input())
txt = ""
if(a-b<0):
    if(a-b==a_b):
        txt="JEDI"
    elif(a-b==a_b*-1):
        txt="SITH"
else:
    txt="VEIT EKKI"
print(txt)