# task 1725
# Difficulty 133

n, k = map(int, input().split())
print(max(0, max(n-k-2, k-3)))
