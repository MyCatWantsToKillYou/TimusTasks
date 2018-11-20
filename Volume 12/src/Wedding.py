# task #2100
# Difficulty 34

guests = 2
for i in range(int(input())):
    if input().endswith('+one'):
        guests += 2
    else:
        guests += 1
if guests == 13:
    print(1400)
else:
    print(guests*100)
