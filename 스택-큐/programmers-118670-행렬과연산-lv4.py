from collections import deque

def solution(rc, operations):
    R, C = len(rc), len(rc[0])
    ROTATE, SHIFT = 0, 1
    
    operations = [ROTATE if op=="Rotate" else SHIFT for op in operations]
    rows = deque(deque(row[1:-1]) for row in rc)
    left = deque(row[0] for row in rc)
    right = deque(row[-1] for row in rc)
    
    for op in operations:
        if op == ROTATE:
            rows[0].appendleft(left.popleft())
            right.appendleft(rows[0].pop())
            rows[-1].append(right.pop())
            left.append(rows[-1].popleft())
        else:
            rows.appendleft(rows.pop())
            left.appendleft(left.pop())
            right.appendleft(right.pop())
    
    for r in range(R):
        rows[r].append(right[r])
        rows[r].appendleft(left[r])
    
    return list(list(row) for row in rows)

