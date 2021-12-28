from itertools import combinations

def solution(relation):
    data_num, attr_num = len(relation), len(relation[0])
    keys, unique_keys = [], []
    
    # 후보키 후보
    for amount in range(1, attr_num + 1):
        keys.extend(map(set, combinations(range(attr_num), amount)))
    
    for key in keys:
        db = set()
        
        for data in relation:
            db.add("".join([data[attr] for attr in key]))
        
        if len(db) != data_num: continue
        
        if is_unique(key, unique_keys):
            unique_keys.append(key)
        
    return len(unique_keys)
    
def is_unique(candidate, unique_keys):
    for key in unique_keys: 
        if key.issubset(candidate): return False
    return True
