def cipher(str):
    cystr=""
    for i in str:
        if i.islower():
            cystr+=(chr(219-ord(i)))
        else:
            cystr+=i
    return cystr


print(cipher("abcddd1"))

print(cipher(cipher("abcddd1")))