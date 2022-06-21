from collections import defaultdict

def solution(enroll, referral, sellers, amounts):
    N = len(enroll)
    answer = [0]*N
    DB = {enroll[i]:i for i in range(N)}
    taxes, sellings = defaultdict(list), defaultdict(list)
    
    for seller, amount in zip(sellers, amounts):
        sellings[seller].append(amount)

    for seller in reversed(enroll):
        seller_id = DB[seller]
        referer = referral[seller_id]
        new_taxes = []

        for amount in sellings[seller]:
            cost, tax = amount*100, amount*10
            answer[seller_id] += [cost-tax, cost][tax == 0]
            if tax != 0: new_taxes.append(tax)
            
        for child_tax in taxes[seller]:
            profit, tax = child_tax, child_tax//10
            answer[seller_id] += [profit-tax, profit][tax == 0]
            if tax != 0: new_taxes.append(tax)
        
        if referer != "-":
            taxes[referer].extend(new_taxes)
    return answer
