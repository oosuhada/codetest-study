def solution(i, j, k):
    answer = ''
    for x in range(i,j+1):
        answer += str(x)

    return answer

# TypeError: can only concatenate str (not "int") to str
# def solution(i, j, k):
#     answer = ''
#     for x in range(i,j+1):
#         answer += x

#     return answer