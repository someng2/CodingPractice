from collections import Counter
import collections

def solution(N, stages):
    result = []
    
    list1 = []
    dict1 = collections.defaultdict(float)
    
    counter = Counter(stages)
        
    members = len(stages)
    for i in range(1,N+1):
        if counter[i] != 0:
            dict1[i] = counter[i]/members
            members -= counter[i]
        else:
            dict1[i] = 0
        
    dict1 = sorted(dict1.items(), key = lambda item: item[1], reverse = True)

    for k,v in dict1:
        result.append(k)
    
    return result
