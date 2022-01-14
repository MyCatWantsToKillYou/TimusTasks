#task 1510
#Difficulty 88
from sys import stdin

n = int(stdin.readline())
element = stdin.readline()
count = 1
for i in range(1, n):
    if count == 0:
        element = stdin.readline()
        count = 1
    else:
        p = stdin.readline()
        if element == p:
            count += 1
        else:
            count -= 1
print(element)