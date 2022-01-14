#Task 1023
#Diff 202


k = int(input())
i = k // 3
while k % i != 0:
    i = k // (k // i + 1)

print(k // i - 1)