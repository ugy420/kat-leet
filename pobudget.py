n = int(input())
budget = []
suma = 0

for _ in range(n):
    desc = input()
    suma += int(input())

if(suma>0):
    print("Usch, vinst")
elif(suma<0):
    print("Nekad")
else:
    print("Lagom")