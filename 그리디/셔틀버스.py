def solution(N, NEXT, MAX, TIMES):
    START, END, idx, ans = 540-NEXT, N*NEXT+(540-NEXT), 0, 0
    TIMES = sorted(to_minute(t) for t in TIMES)
    
    while START + NEXT <= END:
        passengers, START, = 0, START + NEXT
        while idx < len(TIMES) and TIMES[idx] <= START and passengers < MAX:
            idx, passengers = idx + 1, passengers + 1
        ans = START if passengers < MAX else TIMES[idx-1] - 1
    return to_hour_min(ans)

def to_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def to_hour_min(time):
    hour, _min = time // 60, time % 60
    hour = "0" + str(hour) if hour < 10 else str(hour)
    _min = "0" + str(_min) if _min < 10 else str(_min)
    return ":".join((hour, _min))
