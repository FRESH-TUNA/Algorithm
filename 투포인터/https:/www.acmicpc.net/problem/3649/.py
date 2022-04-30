import sys
input = sys.stdin.readline

while True:
    try:
        blank, N = int(input()) * 10000000, int(input())
        blocks = sorted(int(input()) for _ in range(N))
        left, right = 0, N-1
        flag = False
        
        while left < right:
            res = blocks[left] + blocks[right]
            if res == blank:
                flag = True
                print("yes " + str(blocks[left]) + " " + str(blocks[right]))
                break
            elif res > blank: right -= 1
            else: left += 1
        if not flag: print("danger")
    except:
        break