import re
from collections import Counter
def solution(str1, str2):
    
    arr1 = [ str1[i:i+2].lower() for i in range(len(str1)-1) if re.findall(r'[a-zA-Z]{2}', str1[i:i+2])]
    arr2 =  [ str2[i:i+2].lower() for i in range(len(str2)-1) if re.findall(r'[a-zA-Z]{2}', str2[i:i+2])]

    intersection = sum((Counter(arr1) & Counter(arr2)).values())
    union = sum((Counter(arr1) | Counter(arr2)).values())

    if not intersection and not union:
        return 65536
    return int(intersection/union*65536)
