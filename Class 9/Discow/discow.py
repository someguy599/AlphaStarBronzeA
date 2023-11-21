paths = input("")
intersections = 0
counted = []

for letter in range(len(paths)):
    if paths[letter] not in counted:
        counted.append(paths[letter])
        finalindice = 0
        for a in range(letter + 1, len(paths)):
            if paths[letter] == paths[a]:
                finalindice = a
                break
        observed = paths[letter:finalindice+1]
        if len(observed) > 2:
            for character in observed:
                if observed.count(character) == 1:
                    intersections += 1
print(intersections//2)


