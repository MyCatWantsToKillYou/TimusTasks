#task 1100
#Difficulty 45


import sys

n = int(sys.stdin.readline())
d = {str(i): list() for i in range(100, -1, -1)}
for _ in range(n):
    line = sys.stdin.readline()
    key, value = line.split()
    d[value].append(key)

for item in d:
    if d[item]:
        for i in d[item]:
            print(i, item)