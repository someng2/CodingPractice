from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX, maxY = 0, 0
    
    # 테두리가 인접해있는 경우를 대비하여 그래프를 2배수로 그리기!!
    for _, _, x2, y2 in rectangle:
        maxX = max(maxX, x2*2)
        maxY = max(maxY, y2*2)
    
    graph = [[0 for _ in range(maxY+2)] for _ in range(maxX+2)]
    
    # 사각형들 다 내부까지 1로 칠하기
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2, x2*2+1):
            for j in range(y1*2, y2*2+1):
                graph[i][j] = 1

    # 그래프 2중 for문 돌면서 자기자신은 1이고 주위 8개중에 0이 하나라도 있다면 테두리 -> 2로 바꿔줌
    for x in range(maxX+1):
        for y in range(maxY+1):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if graph[x][y] == 1 and graph[i][j] == 0:
                        graph[x][y] = 2
                        break
    
    # 2를 따라서 bfs
    dx = [1,0, 0, -1]
    dy = [0,1, -1, 0]
    que = deque([(cx*2,cy*2,0)])
    
    while que:
        x,y,length = que.popleft()
        graph[x][y] = 1
        
        if x == ix*2 and y == iy*2:
            answer = length//2
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 2:
                que.append((nx,ny,length+1))
                
    return answer
