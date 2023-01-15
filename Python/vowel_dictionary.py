# from itertools import product
# def solution(word):
#     words = []
#     char = ['A', 'E', 'I', 'O', 'U']
#     for i in range(1, 6):
#         for c in product(char, repeat=i):
#             words.append(''.join(list(c)))
#     words.sort()

#     return words.index(word)+1

def solution(word):
    answer = 0
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    li = [5**i for i in range(5)]
    
    for i in range(len(word)-1,-1,-1):
        idx = dic[word[i]]
        for j in range(5-i):
            answer += li[j]*idx
        answer+=1
    return answer
