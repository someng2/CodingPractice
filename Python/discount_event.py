import collections

def solution(want, number, discount):
    answer = 0
    want_dic = collections.defaultdict(int)
    store_dic = collections.Counter(discount[:10])
    
    for i, x in enumerate(want):
        if x not in collections.Counter(discount):
            return 0
        want_dic[x] = number[i]
        
    if sum(number) > len(discount):
        return 0
    
    for i, x in enumerate(discount):
        if i == len(discount) -9:
            break
        
        for key, value in want_dic.items():
            if value > store_dic[key]:
                break
        else:
            answer += 1
        store_dic[x] -= 1
        if i+10 < len(discount):
            store_dic[discount[i+10]] += 1
            
    return answer
