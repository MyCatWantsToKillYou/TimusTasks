#task 1020
#Difficulty 100


import math
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def d(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

sum = 0
pi = math.pi
N, R = map(float, input().split())
points = list()
for _ in range(int(N)):
    point = list(map(float, input().split()))
    points.append(point)
for i in range(len(points)-1):
    sum += d(points[i], points[i+1])
sum += d(points[len(points)-1], points[0])
sum += 2*R*pi
print(toFixed(sum, 2))