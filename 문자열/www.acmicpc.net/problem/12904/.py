from collections import deque

def solution():
    source, dest = list(input()), deque(input())
    A, B, D = "A", "B", True
    
    while len(source) != len(dest):
        removed = dest.pop() if D else dest.popleft()
        D = [D, not D][removed == B]

    if not D:
        dest = reversed(dest)
    print([0, 1][tuple(source) == tuple(dest)])

solution()
