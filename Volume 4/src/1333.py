# task 1333
# Difficulty 216

def d(x1,x2,y1,y2):
    return ((y2-y1)**2+(x2-x1)**2)**0.5


def isInCircle(x, y):
    for item in circles:
        if d(item[0], x, item[1], y) <= item[2]:
            return True
    return False


n = int(input())
circles = list()
j = 0
area = 0

for i in range(n):
    x, y, R = map(float, input().split())
    circles.append([x, y, R])

while j <= 1:
    k = 0
    while k <= 1:
        if isInCircle(j, k):
            area += 0.0001
        k += 0.01
    j += 0.01
print(int(area*100))