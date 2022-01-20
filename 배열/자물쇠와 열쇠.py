def solution(key, lock):
    new_lock = get_lock(len(key), lock)
    keys = [rotated_keys(key, i) for i in range(4)]
    return canopen(new_lock, keys, len(key), len(lock))

def get_lock(len_key, lock):
    NEW_LEN = len(lock)+len_key*2
    new_lock = [[0 for _ in range(NEW_LEN)
                ] for _ in range(NEW_LEN)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i+len_key][j+len_key] = lock[i][j]
    return new_lock

def rotated_keys(k, n):
    for _ in range(n): k = list(zip(*reversed(k)))
    return k

def canopen(lock, keys, len_key, len_rock):
    length = len_rock + len_key
    for i in range(length):
        for j in range(length):
            for key in keys:
                set_key(lock, key, i, j)
                if check(lock, len_key): return True
                set_key(lock, key, i, j)
    return False

def check(lock, len_key):
    for i in range(len_key):
        for j in range(len_key):
            if not lock[len_key+i][len_key+j] == 1: return False
    return True

def set_key(lock, key, k, l):
    for i in range(len(key)):
        for j in range(len(key)):
            lock[k+i][l+j] ^= key[i][j]
