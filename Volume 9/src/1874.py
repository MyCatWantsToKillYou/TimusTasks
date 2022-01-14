#task 1874
#Difficulty 175

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

a, b  = map(int, input().split())
print(toFixed(a*b*2**0.5/2 + (a**2 + b**2)/4, 8))