def solution(key, lock):
    lock = make_lock(len(key), lock)

    return 1

def make_lock(len_key, lock):
    NEW_LEN, X = len(lock)+len_key*2-2, len_key-1
    new_lock = [[0 for _ in range(NEW_LEN)
                ] for _ in range(NEW_LEN)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i+X][j+X] = lock[i][j]
    return new_lock