# task #2056
# Difficulty 58

grades = []
for i in range(int(input())):
    grades.append(int(input()))

if 3 in grades:
    print('None')
elif sum(grades)/len(grades) == 5:
    print('Named')
elif sum(grades)/len(grades) >= 4.5:
    print('High')
else:
    print('Common')


