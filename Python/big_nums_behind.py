def solution(numbers):
#     answer = []
#     stack = []
    
#     for num in numbers[::-1]:
#         for target in stack[::-1]:
#             if num < target:
#                 answer.append(target)
#                 break
#         else:
#             answer.append(-1)
#         stack = list(filter(lambda x: x > num, stack))
#         stack.append(num)

#     return answer[::-1]

    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result
