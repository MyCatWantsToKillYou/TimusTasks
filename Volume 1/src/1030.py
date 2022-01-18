#task 1030
#Difficulty 850

from math import sin, cos, acos
import re

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


CONST_PI = 3.1415926535897932384626433
input()
input()
input()
pattern = r'\d+|\D[A-Z][A-Z]'
shipCoords = input()
shipCoords += input()
result = re.findall(pattern, shipCoords)
letters = []

for item in result:
    if item.strip() == 'NL' or item.strip() == 'SL' or item.strip() == 'EL' or item.strip() == 'WL':
        letters.append(item.strip())
        result.remove(item)


input()
iceCoords = input()
iceCoords += input()
result1 = re.findall(pattern, iceCoords)
letters1 = []

for item in result1:
    if item.strip() == 'NL' or item.strip() == 'SL' or item.strip() == 'EL' or item.strip() == 'WL':
        letters1.append(item.strip())
        result1.remove(item)

decimal = []
decimal1 = []
rads = []
rads1 = []
for i in (0, 3):
    decimal.append(float(result[i]) + float(result[i+2])/3600 + float(result[i+1])/60 )
    decimal1.append(float(result1[i]) + float(result1[i+2])/3600 + float(result1[i+1])/60)
for item in letters:
    if item == 'SL':
        decimal[0] = -decimal[0]
    if item == 'WL':
        decimal[1] = -decimal[1]
for item in letters1:
    if item == 'SL':
        decimal1[0] = -decimal1[0]
    if item == 'WL':
        decimal1[1] = -decimal1[1]

for i in range(2):
    rads.append(decimal[i]*CONST_PI/180.0)
    rads1.append(decimal1[i] * CONST_PI / 180.0)
res = sin(rads[0]) * sin(rads1[0]) + cos(rads[0]) * cos(rads1[0]) * cos(rads[1] - rads1[1])
dist = 3437.5 * acos(round(res, 10))
print('\nThe distance to the iceberg:', toFixed(dist, 2), 'miles.')
if 100.00-dist>0.005:
    print('DANGER!')