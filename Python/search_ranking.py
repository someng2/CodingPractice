from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(infos, queries):
    answer = []
    dictionary = defaultdict(list)

    for info in infos:
        data = info.split(' ')
        conditions = data[:-1]
        score = int(data[-1])

        for n in range(5):
            key_comb = list(combinations(conditions, n))
            for k in key_comb:
                key = ''.join(k)
                dictionary[key].append(score)
    # 점수 기준 정렬
    for x in dictionary:
        dictionary[x] = sorted(dictionary[x])
        
    for query in queries:
        query = query.replace(' and', '').replace('-', '').split(' ')
        key = ''.join(query[:-1])
        value = int(query[-1])

        result = dictionary[key]
        answer.append(len(result) - bisect_left(result, value))

    return answer
