# task #1131
# Difficulty 76

n, k = map(int, input().split())

x = 1
count = 0
while x < k and x < n:
    x <<= 1
    count += 1

if x < n:
    count += (n - x + k - 1)/k
print(int(count))