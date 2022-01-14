#task 1295
#Difficulty 151

n = int(input())
a = 2**n
if n == 1:
    print(1)
elif n % 4 == 0:
    print(0)
elif n % 4 == 3 or n % 5 == 0 and n != 10:
    print(2)
else:
    print(1)