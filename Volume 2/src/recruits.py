# Task 1135
# Difficulty 164

m = int(input())
string = ''
count = 0
pos = 0
lst = []
while pos < m:
    a = input()
    string += a
    pos += len(a)
pos = 0
while pos < len(string):
    if string[pos] == '>':
        lst.append(True)
    else:
        lst.append(False)
    pos += 1
pos = 0
for i in range(m):
    if not lst[i]:
        count += i - pos
        pos += 1
print(count)