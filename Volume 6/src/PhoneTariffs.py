# task #1576
# Difficulty 144


N1, C1 = map(int, input().split())
N2, T, C2 = map(int, input().split())
N3 = int(input())
calls = int(input())
minutes = 0

for i in range(calls):
   mm, ss = map(int, input().split(':'))
   if mm == 0 and ss <= 6:
      continue
   minutes += mm
   if ss != 0:
      minutes += 1

print('Basic:     ' + str(minutes * C1 + N1))
print('Combined:  ' + str(max([0, minutes - T])*C2 + N2))
print('Unlimited: ' + str(N3))
