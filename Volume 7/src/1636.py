# task 1636
# Difficulty 58

qxx, zzz = map(int, input().split())
penalty = list(map(int, input().split()))
acc = 0
for item in penalty:
    acc += item * 20

if zzz-acc >= qxx:
    print('No chance.')
else:
    print('Dirty debug :(')
