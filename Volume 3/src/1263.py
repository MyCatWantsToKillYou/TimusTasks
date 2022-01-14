# task 1263
# Difficulty 44

n, m = input().split()
n = int(n)
m = int(m)
countCandidates = [0] * n
a = []
for i in range(m):
    vote = int(input())
    countCandidates[vote - 1] += 1
for j in range(n):
    print('%.2f' % ((countCandidates[j] / m)*100) + '%')