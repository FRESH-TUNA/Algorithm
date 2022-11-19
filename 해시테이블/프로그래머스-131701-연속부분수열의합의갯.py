def solution(elements):
    N = len(elements)
    elements = elements*2
    answer = set()
    
    for i in range(N):
        candidate = elements[i]
        answer.add(candidate)
        
        for i in range(i+1, i+N):
            candidate += elements[i]
            answer.add(candidate)
            
    return len(answer)

