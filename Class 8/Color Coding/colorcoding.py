N, M = map(int, input("").split(" "))
sequences = []
indices = {}

for i in range(N*2): sequences.append(input(""))

for index in range(0, N):
    info = []
    for sequence in sequences:
        if sequence[index] not in info: info.append(sequence[index])
    indices[index] = info

print(indices)