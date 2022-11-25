import heapq

def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    prev = -1
    now = 0
    i = 0
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if prev < j[0] <= now:
                heapq.heappush(heap, [j[1],j[0]])
        
        if heap:
            duration2, start2 = heapq.heappop(heap)
            prev = now
            now += duration2
            answer += (now - start2)
            i += 1
        else:
            now += 1
            
    return int(answer/len(jobs))
