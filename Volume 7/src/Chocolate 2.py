# task #1639
# Difficulty 34

m, n = map(int, input().split())
if m*n % 2 == 0:
    print('[:=[first]')
else:
    print('[second]=:]')