def solution(n, build_frame):
    answer = set()
    for (x, y, is_bow, install) in build_frame:
        if install:
            answer.add((x, y, is_bow))
            if not valid(answer): answer.remove((x, y, is_bow))
        else:
            answer.remove((x, y, is_bow))
            if not valid(answer): answer.add((x, y, is_bow))      
    return sorted(list(answer))
                
def valid(answer):
    for x, y, is_bow in answer:
        if is_bow:
            if ((x,y-1,0) in answer or (x+1,y-1,0) in answer 
                or ((x-1,y,1) in answer and (x+1,y,1) in answer)):
                continue
            else:
                return False
        else:
            if ((x,y-1,0) in answer 
                or (x-1,y,1) in answer or (x,y,1) in answer 
                or y == 0):
                continue
            else:
                return False
    return True
