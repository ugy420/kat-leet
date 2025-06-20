inp = input()
name = ""

for i in inp:
    if not name or i != name[-1]:
        name += i
print(name)