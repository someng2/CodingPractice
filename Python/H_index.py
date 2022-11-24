def solution(citations):
    n = len(citations)
    answer = n
    citations = sorted(citations, reverse = True)
    for i in range(n):
        if citations[i] <= i:
            return i

    return answer
