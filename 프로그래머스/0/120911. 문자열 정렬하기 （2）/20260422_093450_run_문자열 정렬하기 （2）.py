def solution(my_string):
    answer = []
    for x in my_string:
        if x.isupper:
            answer.append(x.lower())
        else:
            answer.append(x)
    return answer

# TypeError: can only concatenate str (not "builtin_function_or_method") to str
# def solution(my_string):
#     answer = ''
#     for x in my_string:
#         if x.isupper:
#             answer += x.lower
#         else:
#             answer += x
#     answer = answer.sort()
#     return answer

# TypeError: Object of type builtin_function_or_method is not JSON serializable
# def solution(my_string):
#     answer = []
#     for x in my_string:
#         if x.isupper:
#             answer.append(x.lower)
#         else:
#             answer.append(x)
#     return answer