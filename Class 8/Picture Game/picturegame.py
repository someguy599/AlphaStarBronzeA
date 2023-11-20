alphabet = {
"a": 0,"b": 0,
"c": 0,"d": 0,
"e": 0,"f": 0,
"g": 0,"h": 0,
"i": 0,"j": 0,
"k": 0,"l": 0,
"m": 0,"n": 0,
"o": 0,"p": 0,
"q": 0,"r": 0,
"s": 0,"t": 0,
"u": 0,"v": 0,
"w": 0,"x": 0,
"y": 0, "z": 0}

N = int(input(""))
info = []
for i in range(N):
    info.append(list(map(list, input("").lower().split(" "))))

for words in info:
    letters = []
    for word in words:
        for letter in word:
            if letter not in letters: letters.append(letter)
    for character in letters:
        if words[0].count(character) > words[1].count(character): alphabet[character] += words[0].count(character)
        elif words[1].count(character) > words[0].count(character): alphabet[character] += words[1].count(character)
        else: alphabet[character] += words[0].count(character)

for a in alphabet:
    print(alphabet[a])