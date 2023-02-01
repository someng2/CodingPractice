def solution(triangle):
    triangle.reverse()
    
    for h, line in enumerate(triangle):
        if h >= 1 :
            for i, x in enumerate(line):
                triangle[h][i] += max(triangle[h-1][i], triangle[h-1][i+1])
    return triangle[-1][-1]
