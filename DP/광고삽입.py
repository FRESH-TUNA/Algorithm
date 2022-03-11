def solution(play_time, adv_time, logs):
    play_time, adv_time = hms_to_s(play_time), hms_to_s(adv_time)
    logs = [[hms_to_s(t) for t in l.split("-")] for l in logs]

    # 0초부터 play_time초
    db = [0] * (play_time+1)
    
    for (start, end) in logs: 
        db[start] += 1
        db[end] -= 1
    
    # 각 시간대의 동시접속자
    for t in range(1, play_time+1): db[t] += db[t-1]
    
    # 각 시간대의 누적접속자
    for t in range(1, play_time+1): db[t] += db[t-1]
    
    # 값 계산
    res, acc = 0, 0
    if db[adv_time]: acc = db[adv_time]
    
    for t in range(play_time - adv_time + 1):
        if acc < db[t+adv_time] - db[t]: 
            acc = db[t+adv_time] - db[t]
            res = t+1
    
    return s_to_hms(res)
    
def hms_to_s(time):
    h, m, s = [int(t) for t in time.split(":")]
    return h*3600 + m*60 + s

def s_to_hms(time):
    h, time = time // 3600, time % 3600
    m, s = time // 60, time % 60
    
    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(s) if s < 10 else str(s)
    return h + ':' + m + ':' + s
