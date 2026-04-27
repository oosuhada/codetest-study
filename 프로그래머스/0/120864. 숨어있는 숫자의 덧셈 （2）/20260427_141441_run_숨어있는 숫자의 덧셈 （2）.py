def solution(my_string):
    my_list = []
    for c in my_string:
        if c.isdigit:
            my_list.append(c)
        else:
            my_list.append('x')
            
    answer = 0
    return my_list

# 실행한 결괏값 ["a","A","b","1","B","2","c","C","3","4","o","O","p"]이 기댓값 37과 다릅니다. - 왜 replace가 안먹히는지 모르겠음
# def solution(my_string):
#     my_list = []
#     for c in my_string:
#         if c.isdigit:
#             my_list.append(c)
#         else:
#             my_list.append(my_string.replace('',c))
            
#     answer = 0
#     return my_list