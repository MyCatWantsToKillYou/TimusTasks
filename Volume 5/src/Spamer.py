# task #1496
# Difficulty 57

listed = []
for i in range(0, int(input())):
    listed.append(input())
for name in listed:
    a = listed.count(name)
    if a >= 2:
        print(name)
        listed = [x for x in listed if x != name]
