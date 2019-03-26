# task #1490
# Difficulty 205

r = int(input())
x = r
res = 0
for y in range(1, r + 1):
    while (x - 1)**2 + (y - 1)**2 >= r**2:
        x -= 1
    res += x

print(res*4)