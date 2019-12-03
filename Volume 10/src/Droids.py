# task 1991
# Difficulty 44

n, k = map(int, input().split())
spheres = list(map(int, input().split()))
droids = 0
balls = 0

for item in spheres:
    num = k - item
    if num > 0:
        droids += num
    else:
        balls -= num

print(balls, droids)