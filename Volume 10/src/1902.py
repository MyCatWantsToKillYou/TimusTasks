# task 1902
# Difficulty 102
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


n, t, s = map(int,input().split())
i = 0
opp = list(map(int, input().split()))
while i < len(opp):
    if opp[i] >= s:
        print(toFixed((opp[i]+s+t)/2, 6))
    else:
        print(toFixed((opp[i]+s+t)/2, 6))
    i += 1