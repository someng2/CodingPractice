from collections import defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    total_dic = defaultdict(int)
    
    for i, g in enumerate(genres):
        dic[g].append((plays[i], i))
        total_dic[g] += plays[i]

    for genre in sorted(total_dic, key=lambda x:total_dic[x], reverse=True):
        for _, index in sorted(dic[genre], key=lambda x:(x[0], -x[1]), reverse=True)[:2]:
            answer.append(index)
    
    return answer
