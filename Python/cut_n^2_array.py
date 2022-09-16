def solution(n, left, right):
    answer = []
    
    x = int(left/n)
    y = left%n
    # print('x = ', x, 'y = ', y)
    for i in range(right-left+1):
        if y == n:
            y = 0
            x += 1
            
        if x < y: 
            answer.append(y+1)
        else:
            answer.append(x+1)
        y += 1
    return answer
