# task #1446
# Difficulty 93


def printfac(listed, num):
    if num == 0:
        print('Slytherin:')
    elif num == 1:
        print('Hufflepuff:')
    elif num == 2:
        print('Gryffindor:')
    elif num == 3:
        print('Ravenclaw:')
    for item in listed:
        print(item)
    print(' ')


gryff = []
sly = []
huff = []
raven = []
lst = []
for i in range(int(input())):
    name = input()
    fac = input()
    if fac.startswith('S'):
        sly.append(name)
    elif fac.startswith('H'):
        huff.append(name)
    elif fac.startswith('G'):
        gryff.append(name)
    elif fac.startswith('R'):
        raven.append(name)
lst.append(sly)
lst.append(huff)
lst.append(gryff)
lst.append(raven)
for m in range(4):
    printfac(lst[m], m)


