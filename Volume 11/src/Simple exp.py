# task #2066
# Difficulty 29

a = int(input())
b = int(input())
c = int(input())
results = []
results.append(a*b*c)
results.append(a*b+c)
results.append(a*b-c)
results.append(a-b-c)
results.append(a-b*c)
results.append(a-b+c)
results.append(a+b*c)
results.append(a+b-c)
results.append(a+b+c)
print(min(results))