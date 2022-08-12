def solution(s):
    answer = 0
    stack = []

    if len(s) % 2 != 0:
        return 0
    
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if x == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
            
    # print('------------')
    # print('s = ', s)
    # print('stack = ', stack)
    answer = 0 if len(stack) > 0 else 1
    return answer
