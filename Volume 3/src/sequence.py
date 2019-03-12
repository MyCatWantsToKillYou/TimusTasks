# task #1209
# Difficulty 34

ni = 0
numbers = []
m = int(input())
for j in range(m):
    pos = int(input())
    if ((((8*pos)-7)**0.5-1)/2) % 1 == 0:
        numbers.append(1)
    else:
        numbers.append(0)
for num in range(len(numbers)):
    print(numbers[num], end=' ')