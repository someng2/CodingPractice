from collections import defaultdict
from collections import deque

def bfs(dest, way, costs):
    que = deque([dest])
    
    while que:
        x = que.popleft()
        for node in way[x]:
            if costs[node] == -1:
                que.append(node)
                costs[node] = costs[x] + 1
    return costs

def solution(n, roads, sources, destination):
    answer = []
    way = defaultdict(list)
    
    for road in roads:
        way[road[0]].append(road[1])
        way[road[1]].append(road[0])
            
    costs = [-1] * (n+1)
    costs[destination] = 0 
    costs = bfs(destination, way, costs)
    
    for source in sources:
        answer.append(costs[source])
                    
    return answer
