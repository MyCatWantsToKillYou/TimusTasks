# task #1139
# Difficulty 78


def HCF(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a + b


n, m = map(int, input().split())
a = n - 1
b = m - 1

print(a + b - HCF(a, b))