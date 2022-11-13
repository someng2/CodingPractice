from math import gcd

def solution(arrayA, arrayB):
    answer = 0

    # 최대 공약수 구하기
    A, B = get_gcd(arrayA), get_gcd(arrayB)
    
    for i in arrayB:
        if i % A == 0:
            break
    else:
        answer = max(A,answer)
    
    for i in arrayA:
        if i % B == 0:
            break
    else:
        answer = max(B,answer)
    
    return answer

def get_gcd(arr):
    g = arr[0]
    for i in range(1,len(arr)):
        g = gcd(g,arr[i])
    return g
