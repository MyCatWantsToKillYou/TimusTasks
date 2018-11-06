# task #1585
# Difficulty 43

listed = []
count = [0, 0, 0]
for i in range(0, int(input())):
    listed.append(input())
    if listed[i] == 'Emperor Penguin':
        count[0] += 1
    if listed[i] == 'Little Penguin':
        count[1] += 1
    if listed[i] == 'Macaroni Penguin':
        count[2] += 1
if count.index(max(count)) == 2:
    print('Macaroni Penguin')
elif count.index(max(count)) == 1:
    print('Little Penguin')
else:
    print('Emperor Penguin')
