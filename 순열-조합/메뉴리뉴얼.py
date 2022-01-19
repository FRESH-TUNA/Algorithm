# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from typing import Collection

def get_set_menus(orders, menu_counts):
    # dictionary 생성
    menus = {}

    # combination의 결과를 dictionary에다가 넣는다.
    for order in orders:
        for menu in combinations(order, menu_counts):
            menu = ''.join(menu)
            if menu in menus: menus[menu] += 1
            else: menus[menu] = 1
    
    # dictionary의 value가 가장 높은것들을 반환해보자
    menus = sorted(menus.items(), key=lambda t:t[1], reverse=True)
    if len(menus) and menus[0][1] > 1:
        border, maximum_value = 1, menus[0][1]
        while border < len(menus):
            if menus[border][1] < maximum_value: break
            border += 1
        return [menu[0] for menu in menus[:border]]
    else: return []

def solution(orders, course):
    answer = []
    orders = ["".join(sorted(order)) for order in orders]
    for menu_counts in course: 
        answer.extend(get_set_menus(orders, menu_counts))
    return sorted(answer)


## Counter를 활용한 풀이
import collections
import itertools

def solution(orders, course):
    answers = []

    # combination 생성
    for _course in course:
        menus = []
        for order in orders:
            menus.extend(itertools.combinations(sorted(order), _course))

        # 최댓값 찾아서 반환
        menus = collections.Counter(menus).most_common()
        answers.extend([''.join(m) for m, count in menus if count > 1 and count == menus[0][1]])
    
    answers.sort()
    return answers

