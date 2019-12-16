# task #1224
# Difficulty 68

n, m = map(int, input().split())

if m >= n:
    result = 2 * (n - 1)
else:
    result = 2 * (m - 1) + 1

print(result)