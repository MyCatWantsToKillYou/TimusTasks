#task 1214
#Difficulty 100

x, y = map(int, input().split())
if x <= 0 or y <= 0:
    print(x, y)
elif (x + y) % 2 != 0:
   print(y, x)
else:
    print(x, y)