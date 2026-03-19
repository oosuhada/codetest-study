def solution(my_string):
    my_list = []
    for c in my_string:
        my_list.append(c)
    
    new_list = []
    leng = len(my_list)
    for i in range[0:leng]:
        if my_list[i].isupper:
            new_list.append(',')
        elif my_list[i].islower:
            new_list.append(',')
        
            
    answer = 0
    return new_list

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

# c.isdigit: 가 인식이 안되는거 같은데.. 아 .. int를 안썼구나! 적으면서 깨달음
# def solution(my_string):
#     my_list = []
#     for c in my_string:
#         if c.isdigit:
#             my_list.append(c)
#         else:
#             my_list.append('x')
            
#     answer = 0
#     return my_list

# ValueError: invalid literal for int() with base 10: 'a'
# def solution(my_string):
#     my_list = []
#     for c in my_string:
#         if int(c).isdigit:
#             my_list.append(c)
#         else:
#             my_list.append('x')
            
#     answer = 0
#     return my_list

# 실행한 결괏값 [",",",",",",",",",",",",",",",",",",",",",",",",","]이 기댓값 37과 다릅니다. - 숫자도 isupper, islower에 필터링 되나?
# def solution(my_string):
#     my_list = []
#     for c in my_string:
#         if c.isupper:
#             my_list.append(',')
#         elif c.islower:
#             my_list.append(',')
#         else:
#             my_list.append(c)
            
#     answer = 0
#     return my_list