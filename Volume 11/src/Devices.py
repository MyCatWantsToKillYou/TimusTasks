# task 2033
# Difficulty 99

models,prices,recomendations= [],[],[]
for i in range(6):
    name = input()
    model = input()
    price = int(input())
    if model in models:
        if prices[models.index(model)] > price:
            prices[models.index(model)] = price
        recomendations[models.index(model)] += 1
    else:
        models.append(model)
        prices.append(price)
        recomendations.append(1)
if recomendations.count(max(recomendations)) == 1:
    print(models[recomendations.index(max(recomendations))])
else:
    ans = []
    ans1 = []
    l = len(models)
    mm = max(recomendations)
    for i in range(l):
        if recomendations[i] == mm:
            ans.append(models[i])
            ans1.append(prices[i])
    print(ans[ans1.index(min(ans1))])