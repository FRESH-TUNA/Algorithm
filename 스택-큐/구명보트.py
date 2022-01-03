def solution(people, limit):
    people.sort()
    answer = 0
    while people:
        first_person, people, idx = people[0], people[1:], 0
        
        if first_person * 2 > limit: return len(people) + answer + 1
        
        for case in people:
            if first_person + case <= limit: idx += 1
            else: break
        
        if not idx: return len(people) + answer + 1
        
        answer += 1 + len(people) - idx  
        people = people[:idx - 1]
    return answer
