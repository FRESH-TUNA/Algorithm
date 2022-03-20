def solution(s):
    s = ([v.upper() if s[i-1] == " " else v for i, v in enumerate(s.lower())])
    s[0] = s[0].upper()
    return "".join(s)
