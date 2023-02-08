from collections import deque
def solution(scores):
    answer = 1
    wanho = scores[0]
    scores = list(filter(lambda x:x[0]+x[1] >= sum(wanho), scores))
    scores.sort(key=lambda x:(-x[0],x[1]))
    
    maxB = -1
    for x in scores:
        removed = False
        if maxB < x[1]:
            maxB = x[1]

        elif maxB > x[1]:
            removed = True
        if removed:
            if x == wanho:
                return -1
            continue
        if sum(x) > sum(wanho):
            answer += 1

    return answer
        
