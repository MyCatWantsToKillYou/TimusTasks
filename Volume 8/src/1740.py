#task 1740
#Difficulty 138

l, k, h = map(int,input().split())
if l//k != l/k:
    minimum = l//k*h
    maximum = minimum + h
else:
    minimum = l // k * h
    maximum = minimum
print('%.5f' % minimum,'%.5f' % maximum)