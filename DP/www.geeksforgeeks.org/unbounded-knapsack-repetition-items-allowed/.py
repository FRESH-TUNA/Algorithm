import sys

# init
W = 8
val = [10, 40, 50, 70]
wt = [1, 3, 4, 5]

def solution():
    db = [0] * (W+1)
    for v, _w in zip(val, wt):
        for w in range(_w, W+1):
            db[w] = max(db[w-_w]+v, db[w])
    print(db[W])

solution()
