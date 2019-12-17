# task #1581
# Difficulty 42

n = int(input())
h = 1
a = list(map(int, input().split()))
a.append(-1)
for i in range(1, n+1):
    if a[i-1] == a[i]:
        h += 1
    if a[i-1] != a[i]:
        print(str(h) + ' ' + str(a[i-1]), end=' ')
        h = 1