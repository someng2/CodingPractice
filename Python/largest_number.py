from functools import cmp_to_key

def comparator(a,b):
    if str(a)+str(b) > str(b)+str(a):
        return 1
    elif str(a)+str(b) == str(b)+str(a):
        return 0
    else:
        return -1

def solution(numbers):    
    sorted_num = sorted(numbers, key=cmp_to_key(comparator), reverse=True)
    
    if sorted_num[0] == 0:
        return "0"

    return ''.join(str(s) for s in sorted_num)
