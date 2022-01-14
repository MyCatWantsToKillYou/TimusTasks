#task 2111
#Difficulty 66

n = int(input())
costs = list(map(int, input().split()))
i = 0
acc = 0
summary = sum(costs)
while i < n:
    acc += summary*costs[i]
    summary -= costs[i]
    acc += summary*costs[i]
    i += 1
print(acc)