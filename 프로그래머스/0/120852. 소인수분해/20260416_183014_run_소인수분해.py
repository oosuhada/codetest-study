def solution(n):

    answer = []
    for c in range(2,n):
        if n % c == 0:
            answer.append(c)

    return answer

#TypeError: 'int' object is not iterable
# def solution(n):

#     answer = []
#     for c in range(2,n):
#         if n % c == 0:
#             answer += c

#     return answer