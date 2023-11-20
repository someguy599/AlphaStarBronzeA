N, M = map(int, input("").split(" "))
sequencesone = []
sequencestwo = []
indices = 0

for i in range(N): sequencesone.append(input(""))
for j in range(N): sequencestwo.append(input(""))

for index in range(0, M):
    infoone = []
    infotwo = []
    common = 0
    for sequence in sequencesone:
        if sequence[index] not in infoone: infoone.append(sequence[index])
    for sequence in sequencestwo:
        if sequence[index] not in infotwo: infotwo.append(sequence[index])
        
    for letter in infoone:
        if letter in infotwo: common += 1
    
    if common == 0: indices += 1

print(indices)
