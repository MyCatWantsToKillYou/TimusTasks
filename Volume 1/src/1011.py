#Task 1011
#Diff 236


P, Q = map(float, input().split())
P = P / 100
Q = Q / 100
eps = 1e-7
i = 1
while True:
    amo1 = (i / P)
    amo2 = (i / Q)
    if int(amo1-eps) != int(amo2+eps):
        break
    i += 1

print(int(amo2)+1)