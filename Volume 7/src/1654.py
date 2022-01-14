# task 1654
# Difficulty 59

import sys

stack = []
while True:
    c = sys.stdin.read(1)
    if c == "\n":
        break
    if len(stack) == 0 or c != stack[len(stack) - 1] :
        stack.append(c)
    elif c == stack[len(stack) - 1]:
        stack.pop()
print("".join(stack))