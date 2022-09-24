import collections

def solution(survey, choices):
    answer = ''
    dic = collections.defaultdict(int)
    score = 0
    types = ["RT", "CF", "JM", "AN"]
    
    for i, s in enumerate(survey):
        if choices[i] < 4:
            score = abs(choices[i]-4)
            dic[s[0]] += score
        elif choices[i] > 4:
            score = abs(choices[i]-4)
            dic[s[1]] += score
    
    for t in types:
        first = dic[t[0]]
        second = dic[t[1]]
        if first == second:
            answer += t[0]
        else:
            answer += t[0] if first > second else t[1]
    
    return answer
