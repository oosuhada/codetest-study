def solution(my_string):
    answer = ''
    
    for c in my_string:
        if c.isupper == False:
            c.replace(c, c.lower()) 
        else:
            c.replace(c, c.upper()) 
            
    return my_string

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

# 실행한 결괏값 "cccCCC"이 기댓값 "CCCccc"과 다릅니다.
# def solution(my_string):
#     answer = ''
    
#     for c in my_string:
#         if c.isupper == False:
#             c.replace(c, c.upper()) 
#         else:
#             c.replace(c, c.lower()) 
            
#     return my_string