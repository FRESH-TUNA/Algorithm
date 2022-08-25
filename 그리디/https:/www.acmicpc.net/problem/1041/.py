import sys

N = int(input())
dice = list(map(int, sys.stdin.readline().split()))
ans = 0

if N == 1:
    dice.sort()
    for i in range(5):
        ans += dice[i]
else:
    min_lists = [min(dice[0], dice[5]), 
                 min(dice[1], dice[4]), 
                 min(dice[2], dice[3])]
    min_lists.sort()

    one, two, three = min_lists[0], min_lists[0] + min_lists[1], sum(min_lists)
    
    ans += one * (4*(N-2)*(N-1) + (N-2)**2)
    ans += two * (4*(N-1) + 4*(N-2))
    ans += three * 4
print(ans)

