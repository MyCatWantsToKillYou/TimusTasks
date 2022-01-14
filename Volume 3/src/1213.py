#task 1213
#Difficulty 168


gate = input()
comps = set()
while True:
    line = input()
    if line == '#':
        break
    comp1, comp2 = line.split('-')
    comps.add(comp1)
    comps.add(comp2)

print(len(comps)-1 if len(comps) > 0 else 0)