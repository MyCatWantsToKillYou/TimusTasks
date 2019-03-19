# task #1617
# Difficulty 65

m = int(input())
lst = []
cnt = 0
for i in range(m):
    lst.append(input())
b = len(lst)
for item in lst:
    if lst.count(item) // 4 >= 1:
        cnt += lst.count(item) // 4
        lst = list(filter(lambda s: s != item, lst))
    else:
        lst = list(filter(lambda s: s != item, lst))
print(cnt)
