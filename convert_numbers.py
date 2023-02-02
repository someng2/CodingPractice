from collections import deque
def solution(x, y, n):
    
    if x == y:
        return 0
    
    def dfs(x, y, n):
        que = deque([x])
        count[x] = 0
        
        while que:
            x = que.popleft()
            if 0 <= x+n <= 1000000 and count[x+n] == 0:
                count[x+n] = count[x]+1
                que.append(x+n)
            if 0 <= x*2 <= 1000000 and count[x*2] == 0:
                count[x*2] = count[x]+1
                que.append(x*2)
            if 0 <= x*3 <= 1000000 and count[x*3] == 0:
                count[x*3] = count[x]+1
                que.append(x*3)
    
    count = [0] * 1000001
    dfs(x,y,n)

    return count[y] if count[y] else -1
