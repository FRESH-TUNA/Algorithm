import math

def solution(enroll, referral, seller, amount):
    db, db["-"] = {x:i for i,x in enumerate(enroll)}, -1
    childs, ans = make_childs(db, referral), {}
    seller = {db[s]:a for s, a in zip(seller, amount)}
    for i in range(len(enroll)):
        if i not in ans: profit(i, childs, seller, ans)      
    return [ans[i] for i in range(len(enroll))]

def make_childs(db, referral):
    childs = [[] for i in range(len(db) - 1)]
    for child, parent in enumerate(referral):
        if db[parent] == -1: continue
        childs[db[parent]].append(child)
    return childs

def profit(idx, childs, seller, ans):
    self_sell = (seller[idx] * 90 if idx in seller else 0)
    child_sells = sum(math.ceil((ans[c] if c in ans 
                      else profit(c, childs, seller, ans)) // 9 * 0.9)
                      for c in childs[idx])
    ans[idx] = self_sell + child_sells 
    return ans[idx]
