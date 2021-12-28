from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks, bridge, ans = list(reversed(truck_weights)) , deque(), 0
    
    while trucks:
        # bridge가 다차면 하나 방출
        if len(bridge) == bridge_length: weight += bridge.pop()
            
        # 트럭 집어넣기
        next_truck = trucks.pop() if weight >= trucks[-1] else 0
        bridge.appendleft(next_truck)
        weight -= next_truck
        ans += 1
    
    # 마지막 트럭이 빠져나오는것을 합해서 계산
    return ans + bridge_length
