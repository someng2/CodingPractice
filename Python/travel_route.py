def solution(tickets):
    route = []
    stack = ["ICN"]
    dic = defaultdict(list)
    
    for ticket in sorted(tickets):
        dic[ticket[0]].append(ticket[1])
    
    while stack:
        while dic[stack[-1]]:
            stack.append(dic[stack[-1]].pop(0))
        route.append(stack.pop())
    
    return route[::-1]
