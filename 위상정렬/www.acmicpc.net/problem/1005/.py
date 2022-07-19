import sys

def solution():
    input = sys.stdin.readline
    T = int(input())

    def graph(G, M, degrees):
        for _ in range(M):
            first, second = map(int, input().split())
            degrees[second] += 1
            G[first].append(second)

    def init_q(N, q, degrees):
        for i in range(1, N+1):
            if not degrees[i]:
                q.append((i, 0))

    def gaming(N, TIME, G, W, degrees, q):
        answer = [0]*(N+1)
        
        while q:
            building, time = q.pop()
            answer[building] += TIME[building]

            if building == W:
                return answer[building]

            for next_building in G[building]:
                degrees[next_building] -= 1
                answer[next_building] = max(
                    answer[next_building], 
                    time+TIME[building]
                )
                if degrees[next_building] == 0:
                    q.append((next_building, answer[next_building]))

    def service():
        for _ in range(T):
            N, M = map(int, input().split())
            TIME = [0]+list(map(int, input().split()))
            G, degrees, q = [[] for _ in range(N+1)], [0]*(N+1), []
            graph(G, M, degrees)
            W = int(input())
            init_q(N, q, degrees)
            print(gaming(N, TIME, G, W, degrees, q))
    service()

solution()
