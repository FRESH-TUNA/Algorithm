import sys, heapq

def init():
    input = sys.stdin.readline
    N = int(input())
    q = [list(map(int, input().split())) for _ in range(N)]
    q.sort()
    return N, q

def solution(N, q):
    r = []
    heapq.heappush(r, q[0][1])

    for i in range(1, N):
        if q[i][0] < r[0]:
            heapq.heappush(r, q[i][1])
        else:
            heapq.heappop(r)
            heapq.heappush(r, q[i][1])
    print(len(r))

if __name__ == '__main__':
    solution(*init())
