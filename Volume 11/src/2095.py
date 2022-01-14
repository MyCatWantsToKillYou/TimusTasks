#Task 2095
#Diff 222

l, r = map(int,input().split())
cnt = r
i = 2
while True:
    res = cnt
    cnt //= i
    cnt = res - cnt
    if i > cnt:
        break
    i += 1
x = cnt
i = 2
cnt = l - 1
while True:
    res = cnt
    cnt //= i
    cnt = res - cnt
    if i > cnt:
        break
    i += 1
y = cnt
print(x-y)