N, S = map(int, input("").split(" "))
a = []
for l in range(N):
    row = []
    for j in range(N):
        row.append(0)
    a.append(row)

for k in range(N):
    for t in range(k+1):
        a[t][k] = S
        S += 1
        if S == 10: S = 1

for line in a:
    for char in line:
        if char != 0:
            print(f"{char}", end = " ")
        else:
            print(' ', end = " ")
    print('')