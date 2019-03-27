# task #1283
# Difficulty 122

acc, minimum, prc = input().split()
count = 0
acc = int(acc)
minimum = int(minimum)
prc = int(prc)
while acc > minimum:
    acc -= (acc * prc/100)
    count += 1
print(count)