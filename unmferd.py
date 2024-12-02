# m = int(input())
# n = int(input())

# arr = [[0 for j in range(m)] for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         arr[i][j] = input()
# x = 0
# y = 0

# for i in range(n):
#     for j in range(m):
#         if(arr[i][j]=='.'):
#             x+=1
#         elif(arr[i][j]=='#'):
#             y+=1

# if(x!=0 and y!=0):
#     prop = float(x/(x+y))
#     print(prop)


m = int(input())
n = int(input())

arr = [input() for _ in range(n)]

dot = 0
hash_count = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            dot += 1
        elif arr[i][j] == '#':
            hash_count += 1

if dot + hash_count != 0:
    res = dot / (dot + hash_count)
    print(res)
else:
    print("Cannot calculate proportion when both dot and hash counts are zero.")
