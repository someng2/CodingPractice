from collections import Counter
def solution(nums):
    count = Counter(nums)
    if len(count) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(count)
