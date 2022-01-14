#task 1640
#Difficulty 167

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def d(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

n = int(input())
i = 0
X = list()
Y = list()
while i < n:
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    i += 1
medianX = round(sum(X)/n) + 1
medianY = round(sum(Y)/n) + 1
maxD = 0
for j in range(len(X)):
    D = d(medianX, X[j], medianY, Y[j])
    if D > maxD:
        maxD = D

print(medianX, medianY, toFixed(maxD, 10))