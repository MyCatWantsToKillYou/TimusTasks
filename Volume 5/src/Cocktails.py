# task #1402
# Difficulty 135

n = int(input())
amount = 0
for i in range(2, n+1):
    current = 1
    for j in range(n - i + 1, n + 1):
        current = current * j
    amount = amount + current
print(amount)
