import math

def calculate(x1, y1, r1, x2, y2, r2):
    if x1==x2 and y1==y2 and r1==r2:
        return -1
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if (r1+r2)==dist or abs(r1-r2)==dist:
        return 1
    elif (r1+r2)>dist and abs(r1-r2)<dist:
        return 2
    return 0
    
def call():
    for _ in range(int(input())):
        print(calculate(*map(int, input().split())))

call()

