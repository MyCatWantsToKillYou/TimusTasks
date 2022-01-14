#task 1489
#Difficulty 392


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def d(xN, yN, zN, xM, yM, zM):
    return ((xN-xM)**2 + (yN-yM)**2 + (zN - zM)**2)**0.5


A, B, C = map(int, input().split())
firstPoint = list(map(float, input().split()))
secondPoint = list(map(float, input().split()))
points = [firstPoint, secondPoint]
newPoints = []

for point in points:
    if point[0] <= C: #Left side
        newPoints.append(0)
    elif point[0] <= C + A:
        newPoints.append(point[0] - C)
    else:
        newPoints.append(A)
    if point[1] <= B:
        newPoints.append(B-point[1])
    elif point[1] <= B+C:
        newPoints.append(0)
    elif point[1] <= 2 * B + C :
        newPoints.append(point[1] - B - C)
    else:
        newPoints.append(B)

    if (point[1] <= B):
        newPoints.append(0)
    elif point[1] <= B+C and C + A >= point[0] >= C:
        newPoints.append(point[1]-B)
    elif point[0] <= C and point[1] <= 2 * B + C:
        newPoints.append(point[0])
    elif point[0] >= C+A and point[1] <= 2 * B+C:
        newPoints.append(A+C+C - point[0])
    elif point[1] >= B + C + B:
        newPoints.append(2 * (B+C) - point[1])
    else:
        newPoints.append(C)

print(toFixed(d(newPoints[0], newPoints[1], newPoints[2], newPoints[3], newPoints[4], newPoints[5]), 7))