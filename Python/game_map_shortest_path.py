def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    queue = [[0,0]]
    visited = [[-1 for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = 1
    
    if maps[rows-1][cols-2] == 0 and maps[rows-2][cols-1] == 0:
        return -1
    
    while queue:
        x,y = queue.pop(0)
        for a,b in [[x+1,y], [x, y+1], [x-1,y], [x, y-1]]:
            if 0 <= a < rows and 0 <= b < cols and maps[a][b] == 1 and visited[a][b] == -1:
                visited[a][b] = visited[x][y] + 1
                queue.append([a,b])
    
    return visited[rows-1][cols-1]
