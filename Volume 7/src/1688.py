# task 1688
# Difficulty 127

n, m = map(int, input().split())
n = n*3
i = 0
sum = 0
while i < m:
    sum += int(input())
    if sum > n:
        print('Free after ' + str(i+1) + ' times.')
        break
    i += 1
else:
    print('Team.GOV!')