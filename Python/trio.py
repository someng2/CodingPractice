from itertools import combinations

def solution(number):
    answer = 0
    arr = list(combinations(number, 3))
    for x in arr:
        if sum(x) == 0:
            answer += 1
    
    return answer
