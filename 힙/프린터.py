from collections import deque

def solution(priorities, location):
    documents = deque(zip(priorities, range(len(priorities))))
    seq = 1
    
    while documents:
        document = documents.popleft()
        
        if not documents: return seq
        elif document[0] < max(documents, key = lambda x:x[0])[0]: 
            documents.append(document)
        elif document[1] == location: return seq
        else: seq += 1
    return seq
