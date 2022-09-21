def solution(board, skill):
    answer = 0
    rows, cols = len(board), len(board[0])
    arr = [[0 for j in range(cols+1)] for i in range(rows+1)]
    
    # 누적합 세팅
    for t, x1, y1, x2, y2, degree in skill:
        arr[x1][y1] += degree if t == 2 else -degree
        arr[x1][y2+1] += -degree if t == 2 else degree
        arr[x2+1][y1] += -degree if t == 2 else degree
        arr[x2+1][y2+1] += degree if t == 2 else -degree
        
    # 누적합 (행)
    for x in range(rows+1):
        for y in range(cols):
            arr[x][y+1] += arr[x][y]
    
    # 누적합 (열)
    for y in range(cols+1):
        for x in range(rows):
            arr[x+1][y] += arr[x][y]
    
    # board + arr
    for x in range(rows):
        for y in range(cols):
            board[x][y] += arr[x][y]
            if board[x][y] > 0:
                answer += 1
    
    return answer
