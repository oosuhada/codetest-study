def solution(a, b):
    new_a = 0
    new_b = 0
    d = 2
    array = []
    
    for c in range(1,b+1):
        if a // c == 0 and b // c == 0:
            new_a = a / c
            new_b = b / c
    return [new_a, new_b]

    answer = 0



#최대 공약수 구하는 공식이 있을것 같다

# ZeroDivisionError: integer division or modulo by zero
# def solution(a, b):
#     new_a = 0
#     new_b = 0
#     d = 2
#     array = []
#     for c in range(b):
#         if a // c == 0 and b // c == 0 and c >1:
#             new_a = (a // c)
#             new_b = (b // c)

#         while d < new_b:
#             if new_b // d == 0:
#                 array.append(d)
#     answer = 0
#     return array.append

# TypeError: Object of type builtin_function_or_method is not JSON serializable
# def solution(a, b):
#     new_a = 0
#     new_b = 0
#     d = 2
#     array = []
    
#     for c in range(2,b+1):
#         if a // c == 0 and b // c == 0 and c >1:
#             new_a = (a // c)
#             new_b = (b // c)

#         while d < new_b:
#             if new_b // d == 0:
#                 array.append(d)
#     answer = 0
#     return array.append
