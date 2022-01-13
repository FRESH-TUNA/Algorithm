def solution(lines, answer=0):
    for i in range(len(lines)):
        i_t, _answer = lines[i].split()[1], 1
        for j in range(i+1, len(lines)):
            _answer += check(i_t, *lines[j].split()[1:])
        answer = max(_answer, answer)
        if answer >= len(lines) - (i+2): return answer
    return answer

def check(i_e, j_e, j_t):
    j_start = get_start_time(
        *get_time(*j_e.split(":")), float("".join(j_t[:-1])))
    i_end = get_time(*i_e.split(":"))
    return 1 if parallel(*i_end, *j_start) else 0

def get_start_time(j_d, j_h, j_m, j_s, j_t):
    j_s = j_s - j_t + 0.001
    if j_s < 0: j_s, j_m = round(60 + j_s, 3), j_m - 1
    if j_m < 0: j_m, j_h = 60 + j_m, j_h - 1
    if j_h < 0: j_h, j_d = 24 + j_h, j_d - 1
    return (j_d, j_h, j_m, j_s)

def get_time(h, m, s): return (1, int(h), int(m), float(s))

def parallel(i_d, i_h, i_m, i_s, j_d, j_h, j_m, j_s):
    d, h, m, s = j_d-i_d, j_h-i_h, j_m-i_m, round(j_s-i_s, 3)
    if s < 0: s, m = 60 + s, m - 1
    if m < 0: m, h = 60 + m, h - 1
    if h < 0: h, d = 24 + h, d - 1
    return d < 0 or (d == 0 and h == 0 and m == 0 and s < 1)
