from collections import deque

def solution(order):
    answer = 0
    stack = []
    order = deque(order)
    length = len(order)
    x = 1
    
    while x <= length or len(stack) > 0:
        if x == order[0]:
            answer += 1
            order.popleft()
        elif x < order[0]:
            stack.append(x)
        else:
            if len(stack) > 0 and stack[-1] == order[0]:
                answer += 1
                order.popleft()
                stack.pop()
                x -= 1
            elif x > length:
                break

        x += 1

    return answer
