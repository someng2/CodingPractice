cnt = 1
def solution(n, wires):
    global cnt
    answer = float('inf')

    def dfs(graph, visited, start):
        global cnt
        for next_node in graph[start]:
            if not visited[next_node]:
                visited[next_node] = True
                cnt += 1
                dfs(graph, visited, next_node)
    
    for w in wires:
        tmp = wires[:]
        tmp.remove(w)
        graph = [[] for _ in range(n + 1)]
        
        for a, b in tmp:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        networks = []
        for node in range(1, n + 1):
            if not visited[node]:
                visited[node] = True
                cnt = 1
                dfs(graph, visited, node)
                networks.append(cnt)

        answer = min(answer, abs(networks[0] - networks[1]))
    
    return answer
