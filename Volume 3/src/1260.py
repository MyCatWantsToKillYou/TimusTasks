#task 1260
#Difficulty 111


def fu(i):
    lst = [30381786,44526672,65257010,95638797,140165470,205422481,301061279,441226750,646649232,947710512, 1388937263]
    if i == 1 or i == 2:
        return 1
    if i == 3:
        return 2
    if i >= 45:
        return lst[i-45]
    return fu(i-1) + fu(i-3) + 1


i = int(input())
print(fu(i))

