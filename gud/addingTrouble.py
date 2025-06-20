# Taking input as a single line and splitting it into three numbers
a, b, c = map(int, input().split())

# Performing addition and checking equality
sum = a + b
if sum == c:
    print("correct!")
else:
    print("wrong!")
