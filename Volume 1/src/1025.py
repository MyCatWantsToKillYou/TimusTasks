#task 1025
#Difficulty 67


k = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
count = 0
while i < k//2+1:
    count += arr[i]//2+1
    i += 1
print(count)