#task 1049
#Difficulty 241

import sys
mul = 1
i = 2
acc = 1
for x in range(10):
    mul *= int(sys.stdin.readline())
while mul != 1:
    count = 0
    while mul % i == 0:
        mul //= i
        count += 1
    if count != 0:
        acc *=(count+1)
    i += 1
print(acc%10)