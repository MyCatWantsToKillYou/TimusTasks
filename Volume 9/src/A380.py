# task 1893
# Difficulty 55

import re
string = input()

num = re.findall('(\d+)', string)

letter = re.findall('[A-Za-z]', string)

if int(num[0]) <= 2:
    if letter[0] in ('A', 'D'):
        print('window')
    else:
        print('aisle')
elif int(num[0]) <= 20:
    if letter[0] in ('A', 'F'):
        print('window')
    else:
        print('aisle')
else:
    if letter[0] in ('A', 'K'):
        print('window')
    elif letter[0] in ('C', 'D', 'G', 'H'):
        print('aisle')
    else:
        print('neither')