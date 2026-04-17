def solution(s):
    temp_list = []
    for c in s:
        temp_list.append(c)
    answer = ''
    
    for all a in temp_list:
        new_s = s.replace(a,'')
    
    return new_s


# ValueError: not enough values to unpack (expected 2, got 1)
# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
    
#     for a,b in temp_list:
#         if a == b:
#             temp_list.remove(a,b)
#     answer = ''
#     return temp_list

# ValueError: not enough values to unpack (expected 2, got 1)
# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
    
#     for a,b in temp_list:
#         if a == b:
#             temp_list.replace('a','')
#             temp_list.replace('b','')

#     return temp_list