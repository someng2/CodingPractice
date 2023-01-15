def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse = True)
    
    for i, x in enumerate(A):
        answer += (x * B[i])

    return answer
