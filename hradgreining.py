str_input = input()
togg = True

for i in range(len(str_input) - 2):  # Ensure there are at least 3 characters remaining
    if str_input[i] == 'C' and str_input[i+1] == 'O' and str_input[i+2] == 'V':
        togg = False
        break  # No need to continue checking if the substring is found

if togg:
    print("Ekki veikur!")
else:
    print("Veikur!")

# OR
#str_input = input()
# if 'COV' in str_input:
#     print("Veikur!")
# else:
#     print("Ekki veikur!")
