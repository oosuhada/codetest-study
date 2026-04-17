def solution(n):
    answer = []
    
    c = 1
    for c in range[1:n+1]:
        if n % c == 0:
            answer.append(c)
            c += 1
    return answer

# TypeError: 'type' object is not subscriptable
# def solution(n):
#     answer = []
#     for c in range[0:n+1]:
#         if n % c == 0:
#             answer.append(c)
#     return answer