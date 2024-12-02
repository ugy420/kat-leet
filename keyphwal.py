n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = input()

key = False
phone = False
wallet = False

for i in arr:
    if i=="keys":
        key = not key
    elif i=="phone":
        phone = not phone
    elif i=="wallet":
        wallet = not wallet

if key and phone and wallet:
    print("ready")
if not key:
    print("keys")
if not phone:
    print("phone")
if not wallet:
    print("wallet")


