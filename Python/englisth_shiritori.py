def solution(n, words):
    person_idx, idx = 0, 0
    for i, w in enumerate(words):
        if w in words[:i] or (i-1 >= 0 and w[0] != words[i-1][-1]):
            person_idx = (i%n)+1
            idx = (i//n)+1
            break

    return [person_idx, idx]
