# task 1880
# Difficulty 31

input()
a = map(int, input().split())
input()
b = map(int, input().split())
input()
c = map(int, input().split())
print(len(set(a) & set(b) & set(c)))
