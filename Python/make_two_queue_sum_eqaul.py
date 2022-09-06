from collections import deque

def solution(que1, que2):
    result = 0
    sum1 = 0
    sum2 = 0
    
    que1 = deque(que1)
    que2 = deque(que2)
    
    # 모든 원소의 합 계산
    sum1 = sum(que1)
    sum2 = sum(que2)
    total_sum = sum1 + sum2
        
    # 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return
    if (total_sum % 2 != 0):
        return -1
    total_sum /= 2
    
    if sum1 == sum2:
        return 0
    
    while que1 and que2:
        if sum1 == total_sum:
            return result
        
        elif sum1 > total_sum:
            top = que1.popleft()
            sum1 -= top
            result += 1
        else:
            top = que2.popleft()
            que1.append(top)
            sum1 += top
            result += 1
            
    return -1
