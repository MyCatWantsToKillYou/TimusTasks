# task #1567
# Difficulty 42

ad = input()
count = 0
for i in range(0, len(ad)):
        if ad[i] == 'c' or ad[i] == 'f' or ad[i] == 'i' or ad[i] == 'l' or ad[i] == 'o' or \
         ad[i] == 'r' or ad[i] == 'u' or ad[i] == 'x' or ad[i] == '!':
            count += 3
            continue
        if ad[i] == 'b' or ad[i] == 'e' or ad[i] == 'h' or ad[i] == 'k' or ad[i] == 'n' or \
         ad[i] == 'q' or ad[i] == 't' or ad[i] == 'w' or ad[i] == 'z' or ad[i] == ',':
            count += 2
            continue
        else:
            count += 1
            continue
print(int(count))