import math

def solution(n, s):
    answer = []
    multi = 0
    num = s
    index = n
    
    if n > s:
        return [-1]
    
    while num > 0:
        if len(answer) == n-1:
            answer.append(num)
            num = 0
        else:
            answer.append(math.floor(num/index))
            num -= math.floor(num/index)
            index -= 1
    
    return answer
