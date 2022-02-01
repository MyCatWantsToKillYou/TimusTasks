#task 1515
#Difficulty 212

n = int(input())
D = list(map(int, input().split()))
max = 0
for i in range(n):
    if D[i]>max+1:
        print(max+1)
        exit(0)
    else:
        max += D[i]
print(max+1)