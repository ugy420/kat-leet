n = int(input())

# *
# **
# ***
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("")

space = 0

for i in range(n, 0, -2):
    print(" "*space, end="")
    for j in range(i,0,-1):
        print("*", end="")
    print()
    space+=1