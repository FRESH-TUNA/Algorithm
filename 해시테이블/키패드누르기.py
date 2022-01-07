def solution(numbers, hand):
    idxs, hands, answer = ["*", "#"], {"left": 0, "right": 1}, []
    db = {"1": (0, 0, 0), "4": (0, 1, 0), "7": (0, 2, 0), "*": (0, 3, 0),
          "2": (2, 0, 1), "5": (2, 1, 1), "8": (2, 2, 1), "0": (2, 3, 1),
          "3": (1, 0, 2), "6": (1, 1, 2), "9": (1, 2, 2), "#": (1, 3, 2)}
    for n in numbers:
        (typ, x, y), key = db[str(n)], str(n)
        if typ not in (0, 1):
            (l_t, l_x, l_y), (r_t, r_x, r_y) = db[idxs[0]], db[idxs[1]]
            diff = abs(x-l_x)+abs(y-l_y) - (abs(x-r_x)+abs(y-r_y))
            typ = 1 if diff > 0 else (0 if diff < 0 else hands[hand])
        idxs[typ] = key    
        answer.append("L" if typ == 0 else "R")
    return "".join(answer)
