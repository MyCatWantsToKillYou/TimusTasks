widthP, widthC, first, last = map(int, input().split())
print(abs((last - first - 1)*widthP + (last-first)*(widthC*2)))