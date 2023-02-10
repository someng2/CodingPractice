from math import ceil

def solution(n, stations, w):
    answer = 0
    length = 2*w+1
    
    start = 1
    for s in stations:
        answer += max(ceil((s-w-start)/length), 0)
        start = s+w+1
        
    if start <= n:
        answer += max(ceil((n-start+1)/length), 0)

    return answer
