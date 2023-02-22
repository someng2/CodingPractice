from collections import defaultdict

# sol1
# def solution(gems):
#     answer = []
#     num = len(set(gems))
#     counter = defaultdict(int)
#     left = 0
#     for right in range(len(gems)):
#         counter[gems[right]] += 1
#         right += 1
#         while len(counter) == num:
#             counter[gems[left]] -= 1
#             if counter[gems[left]] == 0:
#                 del counter[gems[left]]
#             left += 1
#             answer.append([left, right])
#     answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    
#     return answer[0]

# sol2 - 속도 더 빠름
def solution(gems):
    size = len(set(gems))
    dic = defaultdict(int)
    dic[gems[0]] = 1
    answer = [0, len(gems) - 1]
    start, end = 0, 0

    while(start < len(gems) and end < len(gems)):
        if len(dic) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            dic[gems[end]] += 1

    return [answer[0]+1, answer[1]+1]
