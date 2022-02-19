def solution(play_time, adv_time, logs):
    play_time, adv_time = hms_to_s(play_time), hms_to_s(adv_time)
    logs = [[hms_to_s(l) for l in log.split("-")] for log in logs]
    times = [0] * (play_time+1)
    
    # 시작, 끝시간대에서 동시 접속자
    for (start, end) in logs:
        times[start] += 1
        times[end] -= 1
        
    # 모든 시간대에서의 동시 접속자 계산
    for i in range(1, len(times)): times[i] += times[i-1]

    # 모든 시간대에서의 누적 접속자 계산
    for i in range(1, len(times)): times[i] += times[i-1]
    
    most_view, start_time = 0, 0
    
    if most_view < times[adv_time-1]: most_view = times[adv_time-1]
    
    for i in range(adv_time, play_time):
        if most_view < times[i] - times[i - adv_time]:
            most_view = times[i] - times[i - adv_time]
            start_time = i - adv_time + 1
    return s_to_hms(start_time)

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
    