from itertools import permutations

def solution(ids, bans):
    ans = set("".join(sorted(p)) for p in permutations(
        ids, len(bans)) if fault(p, bans))
    return len(ans)

def fault(ids, bans):
    for _id, ban in zip(ids, bans): 
        if not same(_id, ban): return False
    return True
    
def same(user_id, banned_id):
    if len(user_id) != len(banned_id): return False
    
    for (x, y) in zip(user_id, banned_id):
        if y == "*": continue
        if x != y: return False
    return True
