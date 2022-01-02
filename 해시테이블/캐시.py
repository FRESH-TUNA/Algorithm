from collections import OrderedDict

def solution(cacheSize, cities):
    time, cache = 0, OrderedDict()
    
    for city in map(lambda x: x.lower(), cities):
        if city in cache:
            cache.update({city: True})
            time += 1
        else:
            cache.update({city: True})
            if len(cache) > cacheSize: cache.popitem(last=False)
            time += 5
    return time
