# task #2010
# Difficulty 109

n = int(input())
x, y = map(int, input().split())
king = []
knight = []
bishop = []
rook = []
queen = []


def getBishop(n, x, y):
    amountBishop = 0
    left = x - 1
    right = n - x
    if y+left <= n:
        amountBishop += left
    else:
        amountBishop += n-y
    if y + right <= n:
        amountBishop += right
    else:
        amountBishop += n - y
    if y - left > 0:
        amountBishop += left
    else:
        amountBishop += y - 1
    if y - right > 0:
        amountBishop += right
    else:
        amountBishop += y-1
    return amountBishop


if n == 1:
    king.append(0)
    knight.append(0)
    bishop.append(0)
if n == 2:
    knight.append(0)
if n == 3 and x == 2 and y == 2:
    knight.append(0)
elif n == 3:
    knight.append(2)

if x in (1, n) and y in (1, n):
    king.append(3)
    knight.append(2)
elif x in range(2, n) and y in (1, n) or x in (1, n) and y in range(2, n):
    king.append(5)
else:
    king.append(8)
if x in (1, n) and y in (2, n-1) or x in (2, n-1) and y in (1, n):
    knight.append(3)
elif x in range(3, n-1) and y in (2, n-1) or x in (2, n-1) and y in range(3, n-1):
    knight.append(6)
elif x in range(3, n-1) and y in range(3, n-1):
    knight.append(8)
else:
    knight.append(4)
bishop.append(getBishop(n, x, y))
rook.append(2*n-2)
queen.append(bishop[0]+rook[0])
print('King: ', king[0])
print('Knight: ', knight[0])
print('Bishop: ', bishop[0])
print('Rook: ', rook[0])
print('Queen: ', queen[0])
