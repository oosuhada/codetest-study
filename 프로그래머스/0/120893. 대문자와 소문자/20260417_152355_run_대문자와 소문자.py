def solution(my_string):
    answer = ''
    my_string2 = my_string
    
    for c in my_string2:
        if c.isupper():
            answer += c.lower()
        else:
            answer += c.upper()
            
    return my_string2

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


# ============================================================
# 📌 대소문자 변환 - 핵심 실수 패턴 정리
# ============================================================

# 🔴 실수 1: 메서드 호출 괄호 누락
# c.isupper == True   # ❌ 항상 True (함수 객체 자체는 존재하니까)
# c.isupper == False  # ❌ 항상 False
# answer += c.lower   # ❌ 함수 객체가 더해짐
# answer += c.upper   # ❌ 함수 객체가 더해짐
# if c.isupper():     # ✅ 괄호 필수!
# answer += c.lower() # ✅ 괄호 필수!

# 🔴 실수 2: str.replace()는 원본을 바꾸지 않음
# my_string2.replace(c, c.upper())      # ❌ 반환값을 버리고 있음
# my_string2 = my_string2.replace(...)  # ✅ 반환값을 받아야 함

# ✅ 올바른 풀이 (for loop)
# def solution(my_string):
#     answer = ''
#     for c in my_string:
#         if c.isupper():
#             answer += c.lower()
#         else:
#             answer += c.upper()
#     return answer

# ✅ 올바른 풀이 (한 줄 - swapcase 내장 메서드)
# def solution(my_string):
#     return my_string.swapcase()