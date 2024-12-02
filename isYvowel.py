word = input()

vowel = 0
vowey = 0

for i in word:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel=vowel+1
        vowey = vowey+1
    if(i=='y'):
        vowey = vowey+1
print(str(vowel) + ' ' + str(vowey))