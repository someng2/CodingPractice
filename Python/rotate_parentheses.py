def solution(s):
    answer = 0
    dic = {']': '[', ')': '(', '}': '{' }
    length = len(s)
    stack = list(s)
    
    for x in range(length):
        stack = list(s[x:] + s[:x])
        temp = []
        found = True
        
        while stack:
            s1 = stack.pop()
            # temp 매치
            if s1 not in dic and temp and dic[temp[-1]] == s1:
                temp.pop()
            
            # stack 매치
            elif s1 in dic and stack and stack[-1] == dic[s1]:
                stack.pop()
                
            # 올바르지 않은 문자열
            elif s1 not in dic:
                found = False
                break
                
            else:
                temp.append(s1)

            if len(stack) == 0 and len(temp) == 0:
                answer += 1
                break
    
    return answer
