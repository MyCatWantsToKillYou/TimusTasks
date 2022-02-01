# task 1680
# Difficulty 209

import re
year, n, q = map(int, input().split())
i = 0
names = []
corNames = []
while i < n:
    line = input()
    name = re.sub('\d+| #', '', line)
    if name.lower().strip() not in names:
        names.append(name.lower().strip())
        corNames.append(line)
    i += 1
print(corNames[q])