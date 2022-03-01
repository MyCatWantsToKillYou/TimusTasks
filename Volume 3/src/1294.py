# task 1294
# Difficulty 310
import math


ad, ac, bd, bc = map(int, input().split())
if ad*ac == bd*bc:
    print('Impossible.')
    exit(0)
t1 = (ad**2+ac**2)*2.0*bd*bc-(bd**2+bc**2)*2.0*ad*ac
t2 = 2*bd*bc-2*ad*ac
tt = t1*1.0/t2
if tt < 0:
    print('Impossible.')
else:
    tt = math.sqrt(tt)
    print("Distance is %(tt).0lf km." % {"tt": tt*1000})