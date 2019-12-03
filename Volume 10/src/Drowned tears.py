# task 1935
# Difficulty 72

n = int(input())
count = 0
pages = list(map(int, input().split()))
pages.sort(reverse=True)
pages[0] *= 2
for item in pages:
    count += item
print(count)