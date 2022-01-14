#task 1868
#Difficulty 139

gold = list()
silver = list()
bronze = list()
res = list()
for i in range(12):
    team = input()
    if i<4:
        gold.append(team)
    elif 4<=i<8:
        silver.append(team)
    else:
        bronze.append(team)

n = int(input())
for _ in range(n):
    k = int(input())
    count = 0
    for _ in range(k):
        prediction = input()
        if prediction.endswith('d'):
            teamName = prediction[:prediction.find(":")-1]
            if teamName in gold:
                count += 1
        elif prediction.endswith('r'):
            teamName = prediction[:prediction.find(":") - 1]
            if teamName in silver:
                count += 1
        elif prediction.endswith('e'):
            teamName = prediction[:prediction.find(":") - 1]
            if teamName in bronze:
                count += 1
    res.append(count)

print(sum([5 for x in res if x == max(res)]))