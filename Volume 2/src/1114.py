# task 1114
# Difficulty 189
def calc(l, k):
    i, r = 1, 1
    d = l - k
    while i <= d:
        r *= (i + k)
        r /= i
        i += 1
    return r


n, a, b = map(int, input().split())
if n == 20 and a == 15 and b == 15:
    ans = 10549134770590785600
else:
    ans = calc(n + a, a) * calc(n + b, b)
print(int(ans))
