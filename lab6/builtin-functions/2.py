s= input()
uc = sum(map(str.isupper,s))
lc = sum(map(str.islower, s))
print("Uppercase letters:", uc)
print("Lowercase letters:", lc)