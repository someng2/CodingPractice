import heapq

def solution(scoville, K):
    answer = 0
    
    # scoville 배열이 빌 때까지 while문
    # scoville 배열 sort
    # K 이상일 경우, pop()
    # K 미만일 경우, 그 앞에 있는 애와 계산해서 넣기

    heapq.heapify(scoville)
    
    while len(scoville) > 0:
        x = heapq.heappop(scoville)
        if x < K:
            if len(scoville) > 0:
                y = heapq.heappop(scoville)
                heapq.heappush(scoville, x + 2 *y)
                answer += 1
            else:
                return -1
    
    return answer
