def compress(s):
    count = 0
    prev = ""
    comp = ""

    for i in s:
        if(i==prev or prev==""):
            count+=1
        elif(i!=prev):
            comp += f"{i}{count}" 
            count=0
        prev = i
    return comp

strng = input()
print(compress(strng))

# def compress(s):
#     count = 0
#     prev = ""
#     comp = ""

#     for i in s:
#         if i == prev or prev == "":
#             count += 1
#         else:
#             comp += f"{count}{prev}" if count > 1 else prev
#             count = 1
#         prev = i

#     # Add the last group
#     comp += f"{count}{prev}" if count > 1 else prev

#     return comp if len(comp) < len(s) else s
