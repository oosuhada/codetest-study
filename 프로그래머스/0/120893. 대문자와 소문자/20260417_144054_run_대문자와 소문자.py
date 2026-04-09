def solution(my_string):
    answer = ''
    
    for c in my_string:
        if c.isupper == False:
            answer += c.upper()
        else:
            answer += c.lower()
            
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

# AttributeError: 'str' object has no attribute 'append'
# def solution(my_string):
#     answer = ''
    
#     for c in my_string:
#         if c.isupper == True:
#             answer.append(c.lower)
#         else:
#             answer.append(c.upper)
            
#     return answer

# NameError: name 'upper' is not defined
# def solution(my_string):
#     answer = ''
    
#     for c in my_string:
#         if c.isupper == True:
#             answer += lower(c)
#         else:
#             answer += upper(c)
#     return answer