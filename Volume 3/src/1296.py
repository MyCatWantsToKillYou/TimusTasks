#task 1296
#Difficulty 88

n = int(input())
i = 0
potential = 0
min_sum = 0
ans = 0
while i < n:
    number = int(input())
    potential += number
    ans = max(ans, potential - min_sum)
    min_sum = min(min_sum, potential)
    i += 1
print(ans)