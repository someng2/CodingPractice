def getSubCount(str1, str2):
    count = 0
    for i, x in enumerate(str1):
        if x == str2[i]:
            count += 1
    return count

def solution(begin, target, words):
    answer = 0
    stack = [begin]
    checked = []
    
    if target not in words:
        return 0
    
    while stack:
        cur = stack.pop()
        if cur == target:
            break
        else:
            for x in words:
                if x not in checked and getSubCount(cur,x) == len(begin)-1:
                    stack.append(x)
                    checked.append(x)
        answer += 1
    
    return answer
