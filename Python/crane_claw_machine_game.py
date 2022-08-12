def solution(board, moves):
    
    answer = 0
    N = len(board)
    board_stack = []
    for i in range(N):
        board_stack.append([])
    basket_stack = []
    
    # read 'board' parameter & save in 'board_stack'
    n = 0
    for i in board:
        # n: 0 ~ (N-1)
        # print("n = ", n)
        m = 0
        for j in i:
            if (j != 0):
                board_stack[m].append(j)
            m += 1
        n += 1
    
    # print("board_stack = ", board_stack)
    
    # read 'move' parameter
    num = 0
    for i in moves:
        if board_stack[i-1]:
            num = board_stack[i-1][0]
            # print("num = ", num)
            if (basket_stack):
                if (basket_stack[-1] != num):
                    basket_stack.append(num)
                else:
                    # print("pop() ", basket_stack[-1])
                    basket_stack.pop()
                    answer += 2
            else: 
                basket_stack.append(num)
            board_stack[i-1].pop(0)
        
    return answer
