from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for c in course:
        temp = []
        for order in orders:
            order = sorted(order)
            x = combinations(order, c)
            # print('x = ', list(x))
            temp += x
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            for f in counter: 
                if counter[f] == max(counter.values()):
                    # print('f = ', f)
                    result.append(''.join(f))
            
    return sorted(result)
