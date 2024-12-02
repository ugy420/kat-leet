h,m = map(int,input().split())

if(m>=45):
        m = m - 45
else:
    if(h>0):
        h = h-1
        m = m+60-45
    else:
        h = 23
        m = m+60-45
print(f"{h} {m}")