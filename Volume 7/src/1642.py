#task 1642
#Difficulty 94

n, x = map(int, input().split())
block = list(map(int, input().split()))
pos = [1001]
neg = [-1001]
for item in block:
    if item < 0:
        neg.append(item)
    else:
        pos.append(item)
if x > 0 and min(pos) < x:
    print("Impossible")
elif x < 0 and max(neg) > x:
    print("Impossible")
elif x < 0:
    print(min(pos)*2 + abs(x),end=' ')
    print(abs(x))
elif x > 0:
    print(x, end=' ')
    print(abs(max(neg))*2 + x)