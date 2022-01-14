#task 1120
#Difficulty 87

n = int(input())
if n == 2:
    print(2, 1)
    exit(0)
for P in range(int((2*n)**0.5), 0, -1):
    A = int((2*n - P**2 + P)/(2*P))
    if 2*n % P == 0 and 2*n % (P+2*A - 1) == 0:
        print(A, P)
        break