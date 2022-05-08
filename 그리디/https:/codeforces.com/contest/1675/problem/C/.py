import sys
 
input = sys.stdin.readline
N = int(input())
datas = [input().rstrip() for _ in range(N)]
 
def solution(data):
    left, right = -1, -1
 
    for i in range(len(data)):
        if data[i] == '0':
            left = i
            break
 
    for i in range(len(data)-1, -1, -1):
        if data[i] == '1':
            right = i
            break
 
    if left == -1 and right == -1:
        return len(data)
    elif left == -1:
        return len(data) - right
    elif right == -1:
        return left+1
    else: return left-right+1
    
 
print('\n'.join(str(solution(d)) for d in datas))
