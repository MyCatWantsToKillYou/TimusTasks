# task 1925
# Difficulty 63

n, k = map(int, input().split())
i = 0
last = 0
end = 0
while i < n:
    first, second = map(int,input().split())
    last += first-2-second
    i += 1
end = last + (k-2)
if end < 0:
    print('Big Bang!')
else:
    print(end)