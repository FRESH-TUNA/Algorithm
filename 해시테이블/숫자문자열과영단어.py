def solution(s):
    answer, start, end = [], 0, 1
    NUMBERS = set(str(i) for i in range(10))
    db = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    while end <= len(s):
        if s[start] in NUMBERS: 
            answer.append(s[start])
            start, end = start + 1, start + 2
        elif s[start:end] in db:
            answer.append(db[s[start:end]])
            start, end = end, end + 1
        else: end += 1

    return int("".join(answer))
