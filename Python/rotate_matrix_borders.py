import copy

def solution(rows, columns, queries):
    result = []
    
    # 행렬 저장
    arr = [[(i-1)*columns + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    
    # queries 따라 회전
        # - 최소값 찾아 result에 담기
        
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        temp = arr[x1][y1]
        _min = temp
        
        # 좌측 열
        for k in range(x1, x2):
            n = arr[k+1][y1]
            arr[k][y1] = n
            _min = min(_min, n)
            # print("arr[", k,"][", y1, "] = ", n)
        
        # 하단 행
        for k in range(y1, y2):
            n = arr[x2][k+1]
            arr[x2][k] = n
            _min = min(_min, n)
            # print("arr[", x2,"][", k, "] = ", n)
            
        # 우측 열
        for k in range(x2, x1, -1):
            n = arr[k-1][y2]
            arr[k][y2] = n
            _min = min(_min, n)
            # print("arr[", k,"][", y2, "] = ", n)
            
        # 상단 행
        for k in range(y2, y1, -1):
            n = arr[x1][k-1]
            arr[x1][k] = n
            _min = min(_min,n)
            # print("arr[", x1,"][", k, "] = ", n)
            
        arr[x1][y1+1] = temp
        # print("* arr[", x1,"][", y1+1, "] = ", temp, '\n')
        result.append(_min)
        
    return result
