def solution(s):
    answer = 1001
    
    pattern_count = 1
    # dictionary (key: pattern count(1 ~ ) & value: result string)
    a = {}
    
    if (len(s) == 1):
        answer = 1
        
    while (pattern_count <= len(s) / 2):
        # print('pattern_count = ', pattern_count)
        str1 = ""
        i = 0
        while i < len(s):
            # print('[i = ', i, ']')
            count = 1
            pattern_string = ""
            for k in range(pattern_count):
                if i+k < len(s):
                    pattern_string += s[i+k]
            
            # print('pattern_string = ', pattern_string)
            
            # print('s[i+pattern_count:i+2*pattern_count] = ', s[i+pattern_count:i+2*pattern_count])
            while s[i+pattern_count:i+2*pattern_count] == pattern_string:
                count += 1
                i += pattern_count
                
            if count > 1:
                str1 = str1 + str(count) + pattern_string
            else :
                str1 = str1 + pattern_string
            # print('>> str1 = ', str1)
            
            i += pattern_count
        
        a[pattern_count] = str1
        pattern_count += 1
        # print('----------------------------')
    
    for k, v in a.items():
        if len(v) < answer:
            answer = len(v)
    
    return answer
