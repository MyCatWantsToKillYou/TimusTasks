#task 1123
#Difficulty 119

n = input()
if len(n) == 1:
    print(n)
    exit(0)
if n == n[::-1]:
    print(n)
    exit(0)
if len(n) % 2 != 0:
    if n == len(n) * '9':
        print('1' + '0' * (len(n) - 1) + '1')
    else:
        len_ = len(n[0:(len(n) // 2 + 1)][::-1])
        new_n = str(int(n[0:(len(n) // 2 + 1)]) ) + str(int(n[0:(len(n) // 2 + 1)]) + 1)[::-1][1:(len_ + 1)]
        if int(new_n) > int(n):
            print(new_n)
        else:
            new_n = str(int(n[0:(len(n) // 2 + 1)])+1) + str(int(n[0:(len(n) // 2 + 1)]) + 1)[::-1][1:(len_ + 1)]
            print(new_n)
else:
    new_n = n[0:(len(n) // 2)] + n[0:(len(n) // 2)][::-1]
    if int(new_n) > int(n):
        print(new_n)
    else:
        if n == len(n) * '9':
            print('1' + '0' * (len(n) - 1) + '1')
        else:
            new_n = str(int(n[0:(len(n) // 2)]) + 1) + str(int(n[0:(len(n) // 2)]) + 1)[::-1]
            print(new_n)