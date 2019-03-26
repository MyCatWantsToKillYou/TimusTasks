# task #1423
# Difficulty 183

def kmp(haystack, begin, needle):
    pf = [0]
    k = 0
    for i in range(1, len(needle)):
        while k > 0 and needle[i] != needle[k]:
            k = pf[k-1]
        if needle[i] == needle[k]:
            k += 1
        pf.insert(i, k)
    k = 0
    i = 0
    for i in range(begin, len(haystack)):
        while k > 0 and needle[k] != haystack[i]:
            k = pf[k - 1]
        if needle[k] == haystack[i]:
            k += 1
        if k == len(needle):
            return i - len(needle) + 1
    return -1


n = int(input())
s = input()
t = input()
if s == t:
    print(0)
else:
    s2 = s+s
    pos = kmp(s2, 0, t)
    if pos == -1:
        print(-1)
    else:
        print(n - pos)
