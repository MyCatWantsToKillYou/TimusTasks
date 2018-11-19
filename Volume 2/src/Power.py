# Task 1110
# Difficulty 55

n, m, y = map(int, input().split())
numbers = []
for x in range(m):
    if (x**n) % m == y:
        numbers.append(x)
    else:
        continue
if len(numbers) == 0:
    print(-1)
else:
    for i in range(len(numbers)):
        print(int(numbers[i]), end=' ')

