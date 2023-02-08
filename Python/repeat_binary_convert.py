def solution(s):
    converted = 0
    removed = 0
    
    while s != "1":
        l = s.count("1")
        removed += len(s)-l
        s = bin(l)[2:]
        converted += 1
    
    return [converted, removed]
