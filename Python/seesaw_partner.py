from collections import defaultdict
def solution(weights):
    answer = 0
    ratio = [1, 2, 1/2, 2/3, 3/2, 3/4, 4/3]
    dic = defaultdict(int)
    
    weights.sort()
    for i, w in enumerate(weights):
        if not dic[w]:
            temp = 0
            for j in range(i+1, len(weights)):
                if (w / weights[j]) in ratio:
                    temp += 1
            dic[w] = temp
            answer += temp
        else:
            dic[w] -= 1
            answer += dic[w]

    return answer
