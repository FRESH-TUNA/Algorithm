from collections import defaultdict

def solution(id_list, reports, k):
    count = defaultdict(lambda: 0)
    warning = { name: set() for name in id_list }
    answer = [0]*len(id_list)
    
    for report in reports:
        attacker, defender = report.split()
        if defender not in warning[attacker]:
            warning[attacker].add(defender)
            count[defender] += 1

    for i in range(len(id_list)):
        for defender in warning[id_list[i]]:
            if count[defender] >= k:
                answer[i] += 1
        
    return answer

