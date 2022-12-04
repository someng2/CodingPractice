from collections import defaultdict
def solution(s):
    answer = 0
    string = list(s[::-1])
    
    while string:
        x = string.pop()
        dic = defaultdict(int)
        dic[x] = 1
        dic[0] = 0
        while dic[x] != dic[0] and string:
            if string.pop() == x:
                dic[x] += 1
            else:
                dic[0] += 1
        answer += 1
    return answer
