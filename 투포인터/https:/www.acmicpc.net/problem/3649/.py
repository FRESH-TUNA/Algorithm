import sys
input = sys.stdin.readline

while True:
    try:
        blank, N = int(input()) * 10000000, int(input())
        blocks = sorted(int(input()) for _ in range(N))
        left, right = 0, N-1
        
        while left < right:
            res = blocks[left] + blocks[right]

            if res == blank:
                print("yes " + blocks[left] + " " + blocks[right])
                break
            elif res > blank: right -= 1
            else: left += 1
    except:
        break
    