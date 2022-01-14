#task 1506
#Difficulty 153


n, k = map(int,input().split())
arr = list(map(int, input().split()))
k = int((n+k-1)/k)
i = 0
j = 0
while j < k:
    i = j
    while i < n:
        print(str(arr[i]).rjust(4,' '), end='')
        i += k
    print('')
    j += 1