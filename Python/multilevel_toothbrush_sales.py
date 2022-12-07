from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    answer = []
    relation = defaultdict(str)
    dic = defaultdict(list)
    money = defaultdict(int)
    
    for i, e in enumerate(enroll):
        if referral[i] != '-':
            relation[e] = referral[i]
            dic[e].append(referral[i])
    
    for e, r in list(relation.items()):
        up = r
        while relation[up]:
            dic[e].append(relation[up])
            up = relation[up]
    
    for i, s in enumerate(seller):
        price = amount[i]*100
        if price < 10:
            money[s] += price
            continue
        money[s] += math.ceil(price*0.9)
        price = int(price / 10)
        for up in dic[s]:
            if price < 10:
                money[up] += price
                price = 0
                break
            money[up] += math.ceil(price*0.9)
            price = int(price / 10)   
    
    for e in enroll:
        answer.append(money[e])
    
    return answer
