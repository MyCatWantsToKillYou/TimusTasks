# task 1712
# Difficulty 80


import re


def find(matrix, res):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                res += letters[i][j]
    return res


matrix = []
letters = []
for i in range(4):
    line = input()
    result = re.findall('.', line)
    matrix.append(result)
for i in range(4):
    line = input()
    result = re.findall('.', line)
    letters.append(result)
res=''
for i in range(4):
    res = find(matrix,res)
    matrix = tuple(zip(*matrix[::-1]))
print(res)