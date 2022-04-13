import sys, heapq

def init():
    input = sys.stdin.readline
    N = int(input())
    CARDS = [int(input()) for _ in range(N)]
    heapq.heapify(CARDS)
    return N, CARDS

def solution(N, CARDS):
    res = 0
    card = heapq.heappop(CARDS)

    while CARDS:
        new_card = card + heapq.heappop(CARDS)
        res += new_card
        if not CARDS: break
        heapq.heappush(CARDS, new_card)
        card = heapq.heappop(CARDS)
    print(res)

if __name__ == '__main__':
    solution(*init())
