# task #1576
# Difficulty 144

from datetime import timedelta, datetime

N1, C1 = map(int, input().split())
N2, T, C2 = map(int, input().split())
N3 = int(input())
calls = int(input())
startdate = date = datetime(2019, 3, 5, 0, 0, 0)
limit = startdate + timedelta(minutes=T)

for i in range(calls):
   a = datetime.strptime(input(), "%M:%S")
   delta = timedelta(minutes=a.minute, seconds=a.second)
   if delta > timedelta(seconds=6):
      if delta.seconds % 60 != 0:
         delta = timedelta(minutes=a.minute+1, seconds=0)
         date += delta
      else:
         date += delta

if date.hour != 0:
   minutes = date.hour*60 + date.minute
   print('Basic:     ' + str(date.minute * C1 + N1))
   print('Combined:  ' + str(minutes * C2 + N2))
   print('Unlimited: ' + str(N3))
else:
   print('Basic:     ' + str(date.minute * C1 + N1))
   print('Combined:  ' + str(max([0, date.minute - T])*C2 + N2))
   print('Unlimited: ' + str(N3))
