# task #1493
# Difficulty 51

strin1 = input()
strin = int(strin1)
numberleft = strin-1
numerright = strin+1
strleft = str(numberleft)
strright = str(numerright)
if len(strin1) != len(strleft):
    strleft = strleft.rjust(6, '0')
if len(strin1) != len(strright):
    strright = strright.rjust(6, '0')
left = []
right = []
left1 = []
right1 = []
for i in range(len(strleft)):
    if i < 3:
        left.append(strleft[i])
        left1.append(strright[i])
    else:
        right.append(strleft[i])
        right1.append(strright[i])
if sum(list(map(int, left))) == sum(list(map(int, right))) or sum(list(map(int, left1))) == sum(list(map(int, right1))):
    print('Yes')
else:
    print('No')
