from functools import cmp_to_key

def solution(m, musicinfos):
    m, musicinfos = transform(m), [mu.split(",") for mu in musicinfos]
    musicinfos = [(minute(s, e), n, c) for (s, e, n, c) in musicinfos]
    musicinfos = [(mi, n, transform(c)) for (mi, n, c) in musicinfos]
    musicinfos = [(mi, n, string(mi, c)) for (mi, n, c) in musicinfos]
    musicinfos = list(filter(lambda x: m in x[2], musicinfos))
    musicinfos = [(idx, *v) for idx, v in enumerate(musicinfos)]
    musicinfos.sort(key=cmp_to_key(comparator))
    return musicinfos[-1][2] if musicinfos else "(None)"

def string(minutes, codes):
    d, r = minutes // len(codes), minutes % len(codes)
    return codes * d + codes[:r] 

def minute(s, e):
    s_h, s_m = [int(x) for x in s.split(":")]
    e_h, e_m = [int(x) for x in e.split(":")]
    return (e_h - s_h) * 60 + e_m - s_m

def transform(string):
    return string.replace('C#', 'c').replace('D#', 'd') \
                 .replace('F#', 'f').replace('G#', 'g') \
                 .replace('A#', 'a')

def comparator(x, y):
    return x[1] - y[1] if x[1] != y[1] else y[0] - x[0]
