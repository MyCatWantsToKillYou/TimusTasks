#task 1192
#Difficulty 180

num = int(input())
students, timer, ans = [], 0, 0
for i in range(num):
    student = tuple(map(int, input().split()))
    students.append(student)
students.sort()
for T in students:
    if T[0] > timer:
        timer = T[0]
    timer += T[1]
    dtime = timer - T[2]
    if dtime > ans:
        ans = dtime
print(ans)