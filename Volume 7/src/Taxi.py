# task #1607
# Difficulty 54

a, b, c, d = map(int, input().split())
deal = False
while not deal:
    if a >= c:
        result = a
        deal = True
    else:
        if a + b <= c - d:
            a += b
            c -= d
        else:
            deal = True
            if a + b >= c:
                result = c
            else:
                result = a + b
print(result)