import sys
sys.setrecursionlimit(10**6)

def solution(elements):
    s = set(elements)
    l = len(elements)
    arr = []
    for x in elements:
        arr.append([x])
    elements += elements
    
    def recursive(i, arr):
        cur = i
        for idx, x in enumerate(arr):
            x.append(elements[cur-1])
            s.add(sum(x))
            cur += 1
        if i == l-1:
            return
        recursive(i+1, arr)
            
    recursive(2, arr)
    s.add(sum(elements))

    return len(s) 
