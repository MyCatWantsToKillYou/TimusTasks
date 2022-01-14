# task 1644
# Difficulty 95


from sys import stdin
n = int(input())
i = 0
sat = [10]
hun = []
while i < n:
    num, res = stdin.readline().split()
    if res == 'satisfied':
        if int(num) > 2:
            sat.append(int(num))
        else:
            print('Inconsistent')
            exit(0)
    else:
        hun.append(int(num))
    i += 1
if len(hun) == 0:
    print(min(sat))
elif max(hun) >= min(sat):
    print('Inconsistent')
else:
    print(min(sat))