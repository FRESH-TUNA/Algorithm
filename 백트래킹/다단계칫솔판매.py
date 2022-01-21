import math

def solution(enroll, referral, seller, amount):
    db, db["-"] = {x:i for i,x in enumerate(enroll)}, -1
    seller = [(db[s], a * 100) for s, a in zip(seller, amount)]
    referral, ans = [db[r] for r in referral], [0] * len(enroll)
    for (s, i) in seller: propagate(ans, s, seller, referral, i)
    return ans

def propagate(ans, seller, sellers, referral, income):
    tax = income // 10
    ans[seller] += income - tax
    
    if referral[seller] == -1 or not tax: return
    else: propagate(ans, referral[seller], sellers, referral, tax)
