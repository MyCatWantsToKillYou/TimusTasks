#task 1563
#Difficulty 56


N = int(input())
i = 0
count = 0
magazines = list()
while i < N:
    mag = input()
    if mag not in magazines:
        magazines.append(mag)
    else:
        count += 1
    i += 1
print(count)