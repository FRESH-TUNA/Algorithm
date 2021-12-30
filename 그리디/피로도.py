# https://hkim-data.tistory.com/65
# https://programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    dungeons_count = len(dungeons)
    dungeons_list = [i for i in range(dungeons_count)]
    for i in range(dungeons_count,0,-1):
        for cases in permutations(dungeons_list,i):
            now = k
            check = True
            for case in cases:
                if now < dungeons[case][0]:
                    check = False
                    break
                else:
                    now -= dungeons[case][1]
            if check:
                return i


