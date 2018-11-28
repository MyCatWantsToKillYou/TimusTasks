# task #1545
# Difficulty 56

letters = []

for x in range(int(input())):
    letters.append(input())

let = input()
for i in range(len(letters)):
    if letters[i].startswith(let):
        print(letters[i])

