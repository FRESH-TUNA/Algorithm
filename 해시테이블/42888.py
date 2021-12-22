# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    user_pool = {}
    messages = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    logs = []
    
    # user pool 채우기
    for _record in record:
        _record = _record.split()
        command = _record[0]
        if command in ["Enter", "Change"]:
            uid, uname = _record[1], _record[2]
            user_pool[uid] = uname
        
    # user_pool로 로그 완성하기
    for _record in record:
        _record = _record.split()
        command, uid = _record[0], _record[1]
        if command in ["Enter", "Leave"]:
            logs.append(user_pool[uid] + messages[command])
    return logs