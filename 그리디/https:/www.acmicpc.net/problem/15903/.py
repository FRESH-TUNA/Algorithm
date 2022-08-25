import sys, heapq

input = sys.stdin.readline
N, M = map(int, input().split())
CARDS = list(map(int, input().split()))

heapq.heapify(CARDS)

while M:
    new_card = heapq.heappop(CARDS)+heapq.heappop(CARDS)
    heapq.heappush(CARDS, new_card)
    heapq.heappush(CARDS, new_card)
    M -= 1

print(sum(CARDS))

