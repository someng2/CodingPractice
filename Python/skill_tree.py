import collections
def solution(skill, skill_trees):
    answer = 0
    arr = list(skill)
    
    for tree in skill_trees:
        que = collections.deque(arr)
        for t in filter(lambda x: x in arr, tree):
            if t != que.popleft():
                break
        else:
            answer += 1
    
    return answer
