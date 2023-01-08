import itertools

def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽
                y += 1
            else:   # 대각선 왼쪽
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1

    return list(itertools.chain.from_iterable(answer))
