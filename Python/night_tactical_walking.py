import numpy as np

def solution(distance, scope, times):
    answer = 0
    curr = 0
    firsts = []
    for x,y in scope:
        firsts.append(x)
    scope.sort()
    
    index = np.argsort(firsts)
    times = [times[i] for i in index]
    stop = False
    
    for i, x in enumerate(scope):
        x.sort()
        
        while curr < x[0] -1:
            curr += 1
        
        for n in range(x[0], x[1]+1):
            n %= times[i][0] + times[i][1]

            if n > 0 and n <= times[i][0]:
                curr += 1
                stop = True
                break
            else:
                curr += 1
        else:
            if i == len(scope)-1:
                curr = distance   
        if stop:
            return curr
    return curr
