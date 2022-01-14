# task 1375
# Difficulty 542

import math

A = 0
k, p = map(int, input().split())
while A <= p:
    x = int(math.sqrt(A*p + k))
    y = 0
    if x**2 == A*p + k:
        print(y, x)
        break
    x = int(math.sqrt(A * p + k))
    y = int(math.sqrt(A*p + k - int(x**2)))
    if x**2 + y**2 == A*p + k:
        print(y, x)
        break
    A += 1