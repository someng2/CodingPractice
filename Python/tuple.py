def solution(s):
    result = []
    tup = []
    
    s = s[2:-2]
    s = s.split("},{")
    for x in s:
        tup.append(list(map(int,x.split(','))))
        
    tup.sort(key=len)
    # print('>> tup = ',tup)
    for x in tup:
        for y in x:
            if y not in result:
                result.append(y)
    
    return result
