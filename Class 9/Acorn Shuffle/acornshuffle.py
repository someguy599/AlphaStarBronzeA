'''def shift(originallist):
    newlist = []
    for a in range(1, len(originallist)):
        newlist.append(originallist[a])
    newlist.append(originallist[0])
    return newlist


N = int(input(""))
positions = list(map(int, input("").split(" ")))
unorganized = list(map(int, input("").split(" ")))
acorns = []

for i in range(N):
    position = positions[i] - 1
    acorn = unorganized[i]
    acorns.insert(position, acorn)

print(acorns)'''

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