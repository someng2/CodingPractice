import math

def checkPossible(start, end, bin_str):
    if start == end:
        return bin_str[start]
    mid = (start + end) // 2
    left = checkPossible(start, mid-1, bin_str)
    if not left or (bin_str[mid] == "0" and left == "1"):
        return False
    right = checkPossible(mid+1, end, bin_str)
    if not right or (bin_str[mid] == "0" and right == "1"):
        return False
    if left == "0" and right == "0" and bin_str[mid] == "0":
        return "0"
    return "1"

def solution(numbers):
    answer = []
    for number in numbers:
        bin_str = bin(number)[2:]
        log2 = math.log2(len(bin_str)+1)
        if not log2.is_integer():
            height = int(log2)+1
            bin_str = '0'*(2**height-1-len(bin_str)) + bin_str
        answer.append(1 if checkPossible(0, len(bin_str)-1, bin_str) else 0)
    return answer
