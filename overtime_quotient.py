import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    while n > 0:
        maxWork = heapq.heappop(works)
        heapq.heappush(works, maxWork+1)
        n -= 1
    
    for work in works:
        answer += work**2
    return answer
