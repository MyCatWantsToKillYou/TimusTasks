# task #1083
# Difficulty 71

a = input().split()
b = len(list(a[1]))
m = int(a[0])
res = 1
while m > 1:
    res *= m
    m -= b
print(res)