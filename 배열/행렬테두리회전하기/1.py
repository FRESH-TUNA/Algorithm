# https://programmers.co.kr/learn/courses/30/lessons/77485

def teduri_index(query):
    x1, y1, x2, y2 = query
    a = [[x1, y1 + i] for i in range(y2 - y1)]
    b = [[x1 + i, y2] for i in range(x2 - x1)]
    c = [[x2, y2 - i] for i in range(y2 - y1)]
    d = [[x2 - i, y1] for i in range(x2 - x1)]
    return a + b + c + d

def new_teduri_values(array, teduri_index):
    _teduri_values = [
         array[x][y] for x, y in teduri_index]
    return [_teduri_values[-1]] + _teduri_values[0:len(_teduri_values) - 1]

def array(rows, columns):
    row = [i + 1 for i in range(columns)]
    
    return [[0 for _ in range(columns + 1)]] + [
       [0] + list(map(lambda x: x + i * columns, row)) for i in range(rows)
    ]

         
def solution(rows, columns, queries):
    _array = array(rows, columns)
    answer = []
    for query in queries:
        _teduri_index = teduri_index(query)
        _new_teduri_values = new_teduri_values(
            _array, _teduri_index)
        for index, value in enumerate(_teduri_index):
            x, y = value
            _array[x][y] = _new_teduri_values[index]
        answer.append(min(_new_teduri_values))
    
    return answer



###########
def solution(rows, columns, queries):
    # make_matrix
    matrix = make_matrix(rows, columns)
    # answer
    return [turning_and_min(matrix, query) for query in queries]

def make_matrix(rows, columns):
    border = [[0 for _ in range(columns + 1)]]
    base = [i for i in range(columns + 1)]
    return border + [[value + row * columns for value in base] for row in range(rows)]

def turning_and_min(matrix, query):
    r1, c1, r2, c2 = query
    inserted_value, minimum = matrix[r1][c1], matrix[r1][c1]
    rp, cp = r1, c1 + 1
    
    while not (rp == r1 and cp == c1):
        # swap
        inserted_value_temp = matrix[rp][cp]
        matrix[rp][cp] = inserted_value
        inserted_value = inserted_value_temp
        # minimum
        minimum = min(minimum, inserted_value)
        # rotate
        if rp == r1 and cp < c2: cp += 1
        elif cp == c2 and rp < r2: rp += 1
        elif rp == r2 and cp > c1: cp -= 1
        else: rp -= 1
    
    # last element change and return minimum result
    matrix[rp][cp] = inserted_value  
    return min(minimum, inserted_value)