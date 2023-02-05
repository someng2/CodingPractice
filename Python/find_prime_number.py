from itertools import permutations as permut
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = set([])
    
    # 순열로 1~n개 순열로 숫자 만들어 nums 에 넣기
    for i in range(1, len(numbers)+1):
        for n in list(permut(numbers,i)):
            nums.add(int(''.join(n)))
    
    for n in nums:
        answer += isPrime(n)
    
    return answer
