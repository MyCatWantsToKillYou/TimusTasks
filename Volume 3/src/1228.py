#task 1228
#Difficulty 104

n, s = map(int, input().split())
s -= 1
i = 0
while i < n:
    d = int(input())
    print(s//d, end=" ")
    s %= d
    i += 1