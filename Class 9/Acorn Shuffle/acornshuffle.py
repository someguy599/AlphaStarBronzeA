def shift(originallist, pattern, num):
    newlist = []
    for k in range(num):
        newlist.append(" ")

    for i in range(num):
        position = pattern.index(i+1)
        newlist[position] = originallist[i]
        
    return newlist

N = int(input(""))
pattern = list(map(int, input("").split(" ")))
acorns = list(map(int, input("").split(" ")))

for x in range(3):
    acorns = shift(acorns, pattern, N)

for acorn in acorns:
    print(acorn)
