import math

def solution(n, k):
    answer = 0
    
    if k == 10:
        m = str(n)
    else: 
        # n을 k진법으로 나타내기 -> m
        x = jinsoo(n, k)
        m = str(x)
    
    # m을 0 앞뒤로 잘라서 소수인지 판단
    i = 0
    while i < len(m):
        # print('i = ', i)
        if m[i] != 0:
            temp = ''
            while i < len(m) and m[i] != '0':
                temp += m[i]
                i += 1

            if temp != '' and isPrime(int(temp)):
                answer += 1
            i += 1
        else:
            i += 1
                   
    return answer

def jinsoo(n, k):
    x = ''

    while n > 0:
        n, mod = divmod(n, k)
        x += str(mod)

    return x[::-1] 

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
