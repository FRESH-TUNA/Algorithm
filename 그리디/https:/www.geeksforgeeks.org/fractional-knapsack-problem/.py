s = [[60, 10], [100, 20], [120, 30]]
w = 50

def solution(stuffs, weight):
    stuffs.sort(key=lambda x: x[1] / x[0])
    cur_w, res = 0, 0
    
    for v, w in stuffs:
        if cur_w + w > weight:
            one_kg_v = v // w
            return res + one_kg_v * (weight-cur_w)
        else:
            cur_w += w
            res += v
    return res

print(solution(s, w))
