# task 2073
# Difficulty 196

n = int(input())
i = 0
space = []
while i < n:
    results = {x: ' ' for x in 'ABCDEFGHIJKLM'}
    name = input()
    date = input()
    p, s = map(int, input().split())
    results.update({x: '.' for x in 'ABCDEFGHIJKLM'[0:p]})
    j = 0
    while j < s:
        taskres = list(map(str, input().split()))
        if taskres[1] != 'Accepted' and results[taskres[0]] != 'o':
            results[taskres[0]] = 'x'
        elif taskres[1] == 'Accepted':
            results[taskres[0]] = 'o'
        j += 1
    line = ''
    for item in results.values():
        line += item
    space.append('|'+name.ljust(30)+'|'+date+'|'+line+'|')
    i += 1
print('+------------------------------+--------+-------------+')
print('|Contest name                  |Date    |ABCDEFGHIJKLM|')
print('+------------------------------+--------+-------------+')
for item in space:
    print(item)
    print('+------------------------------+--------+-------------+')