def solution(s):
    temp_list = []
    for c in s:
        temp_list.append(c)
    answer = ''
    
    for a in temp_list:
        s.replace(a,'')
    return temp_list


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