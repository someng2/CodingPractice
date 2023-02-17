# sol1. 스택 이용

def solution(maps):
    answer = []
    arr = []
    
    for m in maps:
        arr.append(list(m))
        
    def isNum(x,y):
        if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y].isdigit():
            return True
        else:
            return False
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if isNum(i,j):
                count = 0
                stack = [[i,j]]
                while stack:
                    x,y = stack.pop()
                    if isNum(x,y):
                        count += int(arr[x][y])
                        arr[x][y] = 'X'
                        if isNum(x+1,y):
                            stack.append([x+1,y])
                        if isNum(x-1,y):
                            stack.append([x-1,y])
                        if isNum(x,y+1):
                            stack.append([x,y+1])
                        if isNum(x,y-1):
                            stack.append([x,y-1])
                answer.append(count)
                
    if not answer:
        return [-1]
    return sorted(answer)

########################################################################################################
# sol2. 재귀함수 이용

import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    arr = []
    
    for m in maps:
        arr.append(list(m))
        
    def isNum(x,y):
        if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y].isdigit():
            return True
        else:
            return False    
    
    def dfs(x,y):
        if isNum(x,y):
            count = int(arr[x][y])
            arr[x][y] = 'O'
            R = dfs(x+1,y)
            L = dfs(x-1,y)
            U = dfs(x,y+1)
            D = dfs(x,y-1)
            return count + R + L + U + D
        else:
            return 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j].isdigit():
                answer.append(dfs(i,j))
    if not answer:
        return [-1]
    
    return sorted(answer)
