# <sol1>
# from collections import deque
# def solution(routes):
#     answer = 0
#     n = len(routes)
#     met = []
#     # routes[i][1] 기준 오름차순 정렬
#     routes = deque(sorted(routes, key=lambda x:x[1]))
    
#     while len(met) < n:
#         camera = routes.popleft()
#         if camera not in met:
#             met.append(camera)
#             answer += 1
#             temp = deque([])
#             while routes:
#                 start, end = routes.popleft()
#                 if [start, end] not in met and start <= camera[1] <= end:
#                     met.append([start, end])
#                 else:
#                     temp.append([start, end])
#             routes = temp + routes

#     return answer

# <sol2>
def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
