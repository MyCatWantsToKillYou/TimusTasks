# task 1313
# Difficulty 37


a = []
b = []
n = int(input())
for k in range(n):
    a = list(map(int, input().split()))
    b.append(a)
for i in range(n):
    for j in range(i + 1):
        print(b[i-j][j], end=' ')
for i in range(n, 2 * n - 1):
    for j in range(n-1, i - n, -1):
        print(b[j][i-j], end=' ')
