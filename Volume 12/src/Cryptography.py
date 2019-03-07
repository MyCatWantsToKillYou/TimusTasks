# task #2102
# Difficulty 115

n = int(input())
if n < 1048576:
    print('No')
    exit()
Ans = []
count = 0
ans = True

for d in range(2, int(n**0.5)+1 and n+1):
    while n % d == 0:
        count += 1
        n //= d
    if count > 20:
        ans = False
        break
    elif count == 20:
        if n != 1:
            ans = False
        break
    elif count == 19:
        if (d+1)*(d+1) > n:
            if d + 1 <= n:
                break
            else:
                ans = False
                break
    if (d + 1)**(20-count) > n:
        ans = False
        break

if ans and n != 1:
    count += 1
if count != 20:
    ans = False

if ans:
    print('Yes')
else:
    print('No')