#task 1319
#Difficulty 40

n = int(input())
def tr(size):
    ans = 0
    for i in range(1, size+1):
        ans += i
    return ans
for j in range(n):
    print()
    for i in range(n):
        if i >= j:
            print((n-i-1)*j + tr(j) + tr(n-i-2) + 1 + j + (n-i-1), end = ' ')
        else:
            print(n*n - (i+1)*(n-j) - tr(n-j-1) - tr(i-1) + 1, end = ' ')