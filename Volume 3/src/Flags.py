# task #1225
# Difficulty 39

lst = []
n = int(input())
for j in range(47):
    lst.append(0)
lst[1] = lst[2] = 2
for i in range(3, 46):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n])