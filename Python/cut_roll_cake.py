from collections import defaultdict
from collections import Counter

def solution(topping):
    answer = 0
    
    dic1 = defaultdict(int)
    dic2 = Counter(topping)
    for i,x in enumerate(topping):
        dic1[x] += 1
        dic2[x] -= 1
        if dic2[x] == 0:
            del dic2[x]
        if len(dic1) == len(dic2):
            answer += 1
        
    return answer
