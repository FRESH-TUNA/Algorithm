def solution(a, b, start=5):
    weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for m in range(1, a+1):
        for n in range(1, month_days[m] + 1):
            if m == a and b == n: return weekday[start]
            else: start = (start + 1) % 7
