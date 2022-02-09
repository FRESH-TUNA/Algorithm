import heapq

def solution(operations):
    min_heap, max_heap, datas = [], [], set()

    for key, operation in enumerate(operations):
        c, arg = operation.split()
        arg = int(arg)
        if c == "I":
            insert(min_heap, max_heap, arg, key, datas)
        else:
            delete(max_heap if arg == 1 else min_heap, datas)
            
    return [peek(max_heap, datas), peek(min_heap, datas)
           ] if len(datas) else [0, 0]

def insert(min_heap, max_heap, arg, key, datas):
    heapq.heappush(min_heap, (arg, arg, key))
    heapq.heappush(max_heap, ((-1) * arg, arg, key))
    datas.add(key)
    
def delete(heap, datas):
    while heap:
        element = heapq.heappop(heap)
        if element[2] not in datas: continue
        datas.remove(element[2])
        return element[1]

def peek(heap, datas):
    while heap:
        element = heap[0]
        if element[2] not in datas:
            heapq.heappop(heap)
            continue
        return element[1]
