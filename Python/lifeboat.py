from collections import deque
def solution(people, limit):
    answer = 0
    que = deque(sorted(people))
    
    while len(que) >= 2:
        if que[0] + que[-1] <= limit:
            que.popleft()
        que.pop()
        answer += 1

    answer += len(que)
    return answer
