import sys, heapq

def solution():
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    degrees, q, answer = [0]*(N+1), [], []

    def graph():
        input = sys.stdin.readline
        for _ in range(M):
            first, second = map(int, input().split())
            degrees[second] += 1
            G[first].append(second)

    def init_heap():
        for i in range(1, N+1):
            if not degrees[i]:
                heapq.heappush(q, i)

    def solving():
        while q:
            question = heapq.heappop(q)
            answer.append(question)

            for next in G[question]:
                degrees[next] -= 1
                if degrees[next]==0:
                    heapq.heappush(q, next)

    graph()
    init_heap()
    solving()
    print(*answer)

solution()
