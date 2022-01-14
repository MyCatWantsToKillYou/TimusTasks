#task 1192
#Difficulty 109


import math

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

g = 10.00
V, a, k = map(float, input().split())
a = a*3.1415926535/180
len = 0
while V > 0.01:
    len = len + V**2 * math.sin(2 * a) / 10
    V /= math.sqrt(k)
print(toFixed(len, 2))