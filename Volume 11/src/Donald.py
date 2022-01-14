# task #2023
# Difficulty 109

position = 'left'
steps = 0
for i in range(int(input())):
    name = input()
    if position == 'center' and name[0] in ('A', 'P', 'O', 'R'):
        position = 'left'
        steps += 1
    elif position == 'center' and name[0] in ('D', 'G', 'J', 'K', 'T', 'W'):
        position = 'right'
        steps += 1
    elif position == 'center' and name[0] in ('B', 'M', 'S'):
        continue
    elif position == 'left' and name[0] in ('B', 'M', 'S'):
        position = 'center'
        steps += 1
    elif position == 'left' and name[0] in ('D', 'G', 'J', 'K', 'T', 'W'):
        position = 'right'
        steps += 2
    elif position == 'left' and name[0] in ('A', 'P', 'O', 'R'):
        continue
    elif position == 'right' and name[0] in ('B', 'M', 'S'):
        position = 'center'
        steps += 1
    elif position == 'right' and name[0] in ('A', 'P', 'O', 'R'):
        position = 'left'
        steps += 2
    else:
        continue
print(steps)
