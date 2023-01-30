def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    connect = set([costs[0][0]])

    while len(connect) < n:
        for i1, i2, cost in costs:
            if i1 in connect and i2 in connect:
                continue
            elif i1 in connect or i2 in connect:
                connect.update([i1, i2])
                answer += cost
                break
    
    return answer
