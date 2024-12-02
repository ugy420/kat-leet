n,k = map(int, input().split(" "))
arr = []
count = 0
arr = input().split(" ")

for i in arr:
    count = count+1
    if(int(i)==k):
        break

if count==1:
    print("fyrst")
elif count==2:
    print("naestfyrst")
else:
    print(f"{count} fyrst")
