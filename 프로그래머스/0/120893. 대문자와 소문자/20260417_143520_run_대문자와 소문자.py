def solution(my_string):
    answer = ''
    
    for c in my_string:
        if c.isupper == True:
            answer.append(c.lower)
        else:
            answer.append(c.upper)
            
    return answer

# TypeError: can only concatenate str (not "builtin_function_or_method") to str
# def solution(my_string):
#     answer = ''
#     for c in my_string:
#         if c.isupper == True:
#             answer += c.lower
#         else:
#             answer += c.upper    
#     return answer