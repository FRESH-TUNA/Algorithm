from collections import deque

def solution(prices):
    answer, prices = [], deque(prices)
    while prices:
        time, price = 0, prices.popleft()
        for _price in prices:
            time += 1
            if _price < price: break
        answer.append(time)
    return answer
