def solution(numbers):
    leng = len(numbers)
    new_list = []
    
    for c in numbers:
        new_list.append(abs(c))
    new_list.sort()
    
    return new_list[leng-2] * new_list[leng-1]


# 마이너스 값은 마이너스 값이어야 하는데 절대값으로 생각함
# def solution(numbers):
#     leng = len(numbers)
#     new_list = []
    
#     for c in numbers:
#         new_list.append(abs(c))
#     new_list.sort()
    
#     return new_list[leng-2] * new_list[leng-1]