def solution(enroll, referral, sellers, amounts):
    N = len(enroll)
    answer = [0]*N
    DB = {enroll[i]:i for i in range(N)}
    
    for seller, amount in zip(sellers, amounts):
        profit, seller_id = amount*100, DB[seller]
        
        while True:
            referer = referral[seller_id]
            for_referer = profit//10
            answer[seller_id] += [profit-for_referer, profit][for_referer == 0]
            
            if referer == "-":
                break
            referer_id = DB[referer]
            seller_id, profit = referer_id, for_referer
    return answer
