# task 1964
# Difficulty 152

n, k = map(int, input().split())
dialects = list(map(int, input().split()))

if sum(dialects)-n*(k-1) <= 0:
    print(0)
else:
    print(sum(dialects)-n*(k-1))
