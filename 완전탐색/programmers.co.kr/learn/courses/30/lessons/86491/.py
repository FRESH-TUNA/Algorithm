def solution(sizes):
    ans_w, ans_h = 0,0
    for w, h in sizes:
        ans_w, ans_h = max(ans_w, max(w, h)), max(ans_h, min(w, h))
    return ans_w*ans_h

