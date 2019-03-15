# task #1290
# Difficulty 81

a =[]
m = int(input())
for m in range(m):
    a.append(int(input()))
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i])