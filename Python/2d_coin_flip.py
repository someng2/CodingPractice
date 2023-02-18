from itertools import product
import sys

def flip(arr, col):
    for row in arr:
        row[col] = 0 if row[col] else 1

def solution(beginning, target):
    answer = sys.maxsize
    flipped = [[0 if element else 1 for element in row] for row in beginning]
    for bit_mask in product([0,1], repeat=len(beginning)):
        new = []
        for i,bit in enumerate(bit_mask):
            new.append(flipped[i][:] if bit else beginning[i][:])
        count = sum(bit_mask)
        for j in range(len(beginning[0])):
            diff = False
            for i in range(len(beginning)):
                if new[i][j] != target[i][j]:
                    diff = True
                    break
            if diff:
                count += 1
                flip(new, j)
        if new == target:
            answer = min(answer, count)
    return -1 if answer == sys.maxsize else answer
