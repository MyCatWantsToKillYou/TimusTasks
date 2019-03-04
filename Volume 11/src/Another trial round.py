# task #2035
# Difficulty 67

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
    a = x
    b = c - a
    print(a, b)