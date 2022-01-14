# task 1573
# Difficulty 104

B, R, Y = map(int,input().split())

ans = 1
n = int(input())
s = []

for i in range(n):
    s.append(input())
    if s[i] == 'Blue':
        ans *= B
    if s[i] == 'Red':
        ans *= R
    if s[i] == 'Yellow':
        ans *= Y
print(ans)
