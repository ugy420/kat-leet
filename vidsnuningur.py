input = input()
i=len(input)-1
revStr = ""

while i>=0:
    revStr += input[i]
    i-=1
print(revStr)