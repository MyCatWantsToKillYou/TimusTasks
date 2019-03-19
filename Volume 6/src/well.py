# task #1572
# Difficulty 144

tp, a = input().split()
tp = int(tp)
a = int(a)
cnt = 0
if tp == 1:
    a = 2*a
elif tp == 2:
    a = a*(2**0.5)

for i in range(int(input())):
    typ, size = input().split()
    typ = int(typ)
    size = int(size)
    if typ == 1:
        size = 2*size
    elif typ == 3:
        size = size * (3**0.5)/2
    if size <= a:
        cnt += 1
print(cnt)