# task #1723
# Difficulty 64

str = input()
i = -1
counts = []
for j in range(1, len(str)):
    count = 0
    while True:
        needle = str[j-1:j]
        i = str.find(needle, i+1)
        if i == -1:
            counts.append(count)
            break
        count += 1
if len(str) == 1:
    print(str)
else:
    print(str[counts.index(max(counts)):counts.index(max(counts))+1])