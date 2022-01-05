import re
from functools import cmp_to_key

def solution(files):
    datas = [split(x) for x in files]
    return [files[i] for i in sorted(range(len(files)), 
        key=cmp_to_key(lambda x, y: compare(x, y, datas)))]

def split(file):
    start, end = re.search(r"[0-9]+", file).span()
    return (file[:start].lower(), int(file[start:end]))

def compare(x, y, datas):
    (x_h, x_n), (y_h, y_n) = datas[x], datas[y]
    if x_h != y_h: return 1 if x_h > y_h else -1
    return x_n - y_n if x_n != y_n else x - y
