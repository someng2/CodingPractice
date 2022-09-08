from itertools import combinations_with_replacement

def solution(n, info):
    result = []
    dif = 0
    
    # 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우)는 [-1] 을 return
    if n == info[0]:
        return [-1]
    if max(info) == 0:
        return [-1]
    
    for arrows in combinations_with_replacement(range(11), n): 
        
        answer = [0] * 11   # 라이언이 맞춘 과녁
        apeach = 0          # 어피치 점수
        lion = 0            # 라이언 점수
        
        for i in arrows:
            answer[10-i] += 1
            
        for i, x in enumerate(answer):
            if x == info[i] == 0:
                continue
            if info[i] >= x:
                apeach += 10-i
            else:
                lion += 10-i
        
        
        if lion - apeach >= dif:
            if lion - apeach > dif:
                # print('라이언 점수 = ', lion)
                # print('어피치 점수 = ', apeach)
                # print('점수 차 = ',lion -apeach)
                dif = lion - apeach
                result = answer
    
    if result:
        return result
    else:
        return [-1]
