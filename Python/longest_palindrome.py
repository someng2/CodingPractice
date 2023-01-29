def isPalindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def solution(s):
    answer = 1
    for length in range(len(s), 1, -1):
        for start in range(len(s)-length+1):
            if s[start] == s[start+length-1] and isPalindrome(s[start:start+length]):
                print(s[start:start+length])
                return length

    return answer
