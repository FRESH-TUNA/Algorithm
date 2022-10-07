import math

def solution(n, stations, w):
    result = 0
    distance = []
    
    for i in range(1, len(stations)):
        distance.append(stations[i]-(w+1)-(stations[i-1]+(w)))
        
    distance.append(stations[0]-(w+1))
    distance.append(n+1-(stations[-1]+(w+1)))
    
    for d in distance:
        if not d: continue
        result += math.ceil(d / (2*w+1))
    return result

