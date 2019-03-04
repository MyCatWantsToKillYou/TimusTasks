# task #2035
# Difficulty 67
#NOT SOLVED YET(TLE 14)

x, y, c = map(int, input().split())
a = 0
b = 0
found = False
if x >= c:
    print(c, 0)
elif y >= c:
    print(0, c)
elif x + y < c:
    print('Impossible')
elif x < c and y < c:
    for i in range(x+1):
        for j in range(y+1):
            if i + j == c:
                a = i
                b = j
                found = True
                break
        if found:
            break
    print(a, b)