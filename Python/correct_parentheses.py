def solution(s):
    answer = True
    stack = []
    origin = []
    
    if len(s) % 2 != 0:
        return False
    
    for x in s:
        origin.append(x)
    
    while len(origin) > 0:
        temp = origin[-1]
        origin.pop()

        if len(stack) > 0:
            if temp != '(' or stack[-1] != ')':
                stack.append(temp)
            else:
                stack.pop()
        else:
            if origin[-1] != '(' or temp != ')':
                stack.append(temp)
                stack.append(origin.pop())
            else:
                origin.pop()
                
    answer = (len(stack) == 0)
    return answer
