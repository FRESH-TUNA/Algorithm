def solution(msg):    
    db = {chr(v): i+1 for i, v in enumerate(range(ord("A"), ord("Z") + 1))}
    answer, start_idx, end_idx = [], 0, 1

    while start_idx < len(msg) and end_idx <= len(msg):
        if msg[start_idx:end_idx] not in db:
            db_answer_update(answer, db, msg, start_idx, end_idx)
            start_idx = end_idx - 1
            end_idx = start_idx + 1
        else: end_idx += 1

    if start_idx != end_idx: 
        db_answer_update(answer, db, msg, start_idx, end_idx)
    return answer

def db_answer_update(answer, db, msg, start_idx, end_idx):
    answer.append(db[msg[start_idx:end_idx - 1]])
    db[msg[start_idx:end_idx]] = len(db) + 1
