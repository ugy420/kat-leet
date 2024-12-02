n = input()
words = input().split()
abb = ""
for word in words:
    if word[0].isupper():
        abb += word[0]
print(abb)