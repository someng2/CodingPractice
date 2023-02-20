from collections import defaultdict

def solution(s, skip, index):
    answer = ''
    lists = list('abcdefghijklmnopqrstuvwxyz')
    index_dic = defaultdict(int)
    for c in skip:
        lists.remove(c)
    for i,c in enumerate(lists):
        index_dic[c] = i
    for c in s:
        answer += lists[(index_dic[c]+index) % len(lists)]

    return answer
