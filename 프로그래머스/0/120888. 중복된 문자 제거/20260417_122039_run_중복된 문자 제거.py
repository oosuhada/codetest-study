def solution(my_string):
    #중복인지를 판별하는게 중요할듯 -> set 사용?

    temp_list = list(my_string)
    answer_list = []
    
    for c in temp_list:
        if c not in answer_list:
            answer_list.append(c)
    
    answer = ''
    for a in answer_list:
        answer += a
    
    return answer


#["e","o","p","l"] 이렇게 set으로 순서가 바뀌어버림
# temp_list = list(my_string)
# temp_list2 = list(set(temp_list))

# answer = ''
# return temp_list2

# TypeError: 'builtin_function_or_method' object is not subscriptable
# temp_list = list(my_string)
# answer_list = []
# for c in temp_list:
#     if c not in answer_list:
#         answer_list.append[c]
# return answer_list

# AttributeError: 'list' object has no attribute 'join'
# return answer_list.join()