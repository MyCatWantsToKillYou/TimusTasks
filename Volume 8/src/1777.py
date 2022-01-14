#task 1777
#Difficulty 114

stones = list(map(int, input().split()))
minimum = 23456245634435642362423234
i = 1
j = 0
count = 0
while True:
    i = j+1
    current = stones[j]
    while i < len(stones):
        diff = abs(stones[i] - current)
        if diff == 0:
            print(count+1)
            exit(0)
        if diff < minimum:
            minimum = diff
        i += 1
    j += 1
    if j == len(stones):
        stones.append(minimum)
        count += 1
        j = 0