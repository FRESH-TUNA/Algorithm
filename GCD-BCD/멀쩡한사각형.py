from math import gcd

def solution(w,h):
    # 최대 공약수
    _gcd = gcd(w, h)
    
    # n + m - 1
    return w * h - ((w // _gcd) + (h // _gcd) - 1) * _gcd
