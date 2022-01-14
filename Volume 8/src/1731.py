#task 1731
#Difficulty 98

n, m = map(int, input().split())
for i in range(1, n+1):
    print(i, end=' ')
print('\n', end='')
for i in range(100, (m+1)*100, 100):
    print(i, end=' ')