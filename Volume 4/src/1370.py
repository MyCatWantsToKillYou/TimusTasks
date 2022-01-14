# task 1370
# Difficulty 92


n, m = map(int,input().split())
numbers = []
result = ''
for i in range(n):
    numbers.append(input())
if m >= n:
    m = m % n
k = 0
j = m
while k < 10:
    if j >= n:
        j = 0
    result += numbers[j]
    k += 1
    j += 1
print(result)