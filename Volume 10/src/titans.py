# task 1910
# Difficulty 34

m = int(input())
a = list(map(int, input().split()))
d = {}

for i in range(m-2):
    d[i+1] = a[i]+a[i+1]+a[i+2]

v = list(d.values())
k = list(d.keys())
print(max(v), k[v.index(max(v))]+1)