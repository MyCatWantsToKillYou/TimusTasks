#task 1196
#Difficulty 55

import sys

count = 0
teacher = set()
for i in range(int(sys.stdin.readline())):
    teacher.add(sys.stdin.readline())


for j in range(int(sys.stdin.readline())):
    if sys.stdin.readline() in teacher:
        count += 1

print(count)