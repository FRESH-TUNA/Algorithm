import sys, math

# init
input = sys.stdin.readline
_, T = int(input()), int(input())
datas = sorted(set(map(int, input().split())))

def solution():
    edges = sorted([(datas[i], datas[i+1]) for i in range(len(datas)-1)], 
                key=lambda x: x[1]-x[0], reverse=True)
    res, count = datas[-1] - datas[0], 1

    for x, y in edges:
        if count >= T: break
        count += 1
        res -= (y-x)
    print(res)
    
solution()
