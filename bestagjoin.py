n = int(input())
name = [0]*n
marks = [0]*n

for i in range(n):
    name[i], marks[i] = input().split()
    marks[i] = int(marks[i])

max = 0
found = ""

for i in range(n):
    if max<marks[i]:
        max = marks[i]

for i in range(n):
    if max == marks[i]:
        found = name[i]
print(found)