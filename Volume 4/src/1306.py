# task 1964
# Difficulty 117

n = int(input())
i = 0
lst = list()
while i <= n/2:
    lst.append(int(input()))
    i += 1
lst.sort()
print(lst)