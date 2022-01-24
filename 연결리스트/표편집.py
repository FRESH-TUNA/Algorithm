def solution(n, k, cmd):
    db = {i: [i-1, i+1] for i in range(n)}
    ans, stack = ["O"] * n, []

    for c in cmd:
        if c[0] == 'D':
            _k = int(c[2])
            while _k: _k, k = _k-1, db[k][1]
        elif c[0] == 'U':
            _k = int(c[2])
            while _k: _k, k = _k-1, db[k][0]
        elif c[0] == 'C':
            (prev, _next), ans[k] = db[k], "X"
            if prev != -1: db[prev][1] = _next
            if _next != n: db[_next][0] = prev
            stack.append([k, prev, _next])
            k = _next if _next != n else prev
        elif c[0] == 'Z':
            (_k, p, _n), ans[_k] = stack.pop(), "O"
            if p != -1: db[p][1] = _k
            if _n != n: db[_n][0] = _k

    return "".join(ans)

