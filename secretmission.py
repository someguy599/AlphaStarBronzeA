name = input("").strip()
namenum = 1

code = input("").strip()
codenum = 1

for a in name:
    print(a, ord(a)-96)

for b in code:
    print(b, ord(b)-96)

namenum = namenum % 47
codenum = codenum % 47

if namenum == codenum: print("GO", namenum, codenum)
else: print("STAY", namenum, codenum)