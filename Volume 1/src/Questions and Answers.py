# task #1026
# Difficulty 147
a = []
c = []
for i in range(int(input())):
  a.append(int(input()))
a.sort()
input()
q = int(input())
for m in range(q):
    c.append(a[int(input())-1])
for j in range(len(c)):
    print(c[j])


