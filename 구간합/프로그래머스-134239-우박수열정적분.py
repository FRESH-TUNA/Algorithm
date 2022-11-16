def solution(k, ranges):
    height, acc = [k], [k]
    answer = []
    
    while height[-1] != 1:
        height.append(height[-1]*3+1 if height[-1]&1 else height[-1]//2)
        acc.append(height[-1])
    
    for i in range(1, len(height)):
        acc[i] += acc[i-1]
    
    for start, end in ranges:
        end = len(height)-1+end
        answer.append(-1.0 if start>end else acc[end]-acc[start]-height[end]/2+height[start]/2)

    return answer

