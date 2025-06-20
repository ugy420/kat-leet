arr = [1,4,3,2,5,1,6,3]
nonDup = []


for i in range(len(arr)):
    if arr[i] not in nonDup:
        nonDup.append(arr[i])

print(nonDup)