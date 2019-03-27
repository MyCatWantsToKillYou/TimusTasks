# task #2011
# Difficulty 84


def factor(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


m = int(input())
lst = list(map(int, input().split()))
st = list(set(lst))
count = factor(m)
for j in range(len(st)):
    count = count/factor(lst.count(st[j]))
if int(count) >= 6:
    print('Yes')
else:
    print('No')