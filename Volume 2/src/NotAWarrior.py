# task #1197
# Difficulty 30

cells = []
for i in range(int(input())):
    pos = input()
    if pos[0] in ('a', 'h') and int(pos[1]) in (1, 8):
        cells.append(2)
    elif pos[0] in ('c', 'd', 'e', 'f') and int(pos[1]) in (3, 4, 5, 6):
        cells.append(8)
    elif pos[0] in ('c', 'd', 'e', 'f') and int(pos[1]) in (2, 7) \
            or pos[0] in ('b', 'g') and int(pos[1]) in (3, 4, 5, 6):
        cells.append(6)
    elif pos[0] in ('a', 'h') and int(pos[1]) in (2, 7) \
            or pos[0] in ('b', 'g') and int(pos[1]) in (1, 8):
        cells.append(3)
    else:
        cells.append(4)

for x in cells:
    print(x)
