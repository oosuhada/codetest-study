def solution(my_string):
    new_list = []
    
    for c in my_string:
        if c.isupper():
            new_list.append(' ')
        elif c.islower():
            new_list.append(' ')
        else:
            new_list.append(c)
    
    joined = ''.join(new_list)  
    parts = joined.split()         # → ['1', '2', '34']  (공백 여러개도 알아서 처리!)
    
    return sum(int(n) for n in parts)



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

# TypeError: 'type' object is not subscriptable
# def solution(my_string):
#     my_list = []
#     for c in my_string:
#         my_list.append(c)
    
#     new_list = []
#     leng = len(my_list)
#     for i in range[0:leng]:
#         if my_list[i].isupper:
#             new_list.append(',')
#         elif my_list[i].islower:
#             new_list.append(',')
#         else:
#             new_list.append(my_list[i])
        
#     answer = 0
#     return new_list

# 계속 오류가 나서 gpt한테 물어보고 c.isupper(), c.islower(), c.isdigit()의 올바른 사용법 복습
# for i in range(leng):  # range는 [] 아니라 () 도 마찬가지로 복습

# parts = joined.split() 방식 효율적이라고 gpt한테 도움 받음