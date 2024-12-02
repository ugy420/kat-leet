n = int(input())
hdist = map(int,input().split())
count = 0
for x in hdist:
    for i in range(1,7):
        for j in range(1,7):
            if(i+j==x):
                count+=1
per = float(count/36)
print(per)