#NOT SOLVED YET

k = int(input())
badwords = []
text = []
positions = []
stringNumbers = []
for i in range(k):
    try:
        badwords.append(input())
    except EOFError:
        ...
m = int(input())
for j in range(m):
    try:
        text.append(input())
    except EOFError:
        ...
found = False
for n in range(len(badwords)):
    for a in range(len(text)):
        if badwords[n] in text[a]:
            stringNumbers.append(a+1)
            positions.append(text[a].find(badwords[n])+1)
            found = True
            break
if found:
    print(min(stringNumbers), min(positions))
else:
    print('Passed')