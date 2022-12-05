from itertools import combinations as combi

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    # 전체 조합
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combi(range(col), i))

    # 유일성
    unique = []
    for candi in candidates:
        tmp = []
        for item in relation:
            tmp.append(tuple([item[i] for i in candi]))
        if len(set(tmp)) == row:
            unique.append(candi)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)
