name = input("").strip().lower()
namenum = 1

code = input("").strip().lower()
codenum = 1

for a in name:
    namenum *= (ord(a) - 96)

for b in code:
    codenum *= (ord(b) - 96)

if namenum % 47 == codenum % 47: print("GO")
else: print("STAY")
