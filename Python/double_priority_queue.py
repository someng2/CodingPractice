import heapq

def solution(operations):
    answer = [0,0]
    heap = []
    
    for operation in operations:
        category, num = operation.split(" ")
        if category == "I":     # 삽입
            heap.append(int(num))
            heapq.heapify(heap)
        elif len(heap) > 0 and num == "1":    # 최대값 삭제
            heap.remove(heapq.nlargest(1,heap)[0])
        elif len(heap) > 0:                   # 최소값 삭제
            heapq.heappop(heap)
            heapq.heapify(heap) 
    if len(heap) == 0:
        return [0,0]
    else:
        min_ = heapq.heappop(heap)
        max_ = heapq.nlargest(1,heap)[0] if len(heap) > 0 else min_
        answer = [max_, min_]
    
    return answer
