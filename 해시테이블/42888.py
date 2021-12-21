def solution(record):
    user_pool = dict()
    log_pool = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    logs = []
    
    for _record in record:
        command, uid = _record[0], _record[1]
        if command == "Change":
            user_pool.update({uid: _record[2]})
        else:
            logs.append([uid, log_pool[command]])
    
    for i in range(len(logs)):
        logs[i] = user_pool[logs[i][0]] + logs[i][1]
    
    return logs
