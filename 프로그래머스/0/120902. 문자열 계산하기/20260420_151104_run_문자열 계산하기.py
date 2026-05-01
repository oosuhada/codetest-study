def solution(my_string):
    my_list = my_string.split()
    return my_list

    
    
    # 01234 -> 2 -> 0,4
    # 012345678910 -> 
# def solution(my_string):
#     answer = ','.join(my_string)
#     a = int(answer[0])
#     c = answer[4]
#     b = int(answer[8])
    
#     if c == '+':
#         return a + b
#     else:
#         return a - b

# def solution(my_string):
#     my_list = my_string.split()
#     if my_list[1] == "+":
#         return int(my_list[0]) + int(my_list[2])
#     elif my_list[2] == "+":
#         return int(my_list[0]) + int(my_list[1]) + int(my_list[3]) + int(my_list[4])
#     elif my_list[1] == "-":
#         return int(my_list[0]) - int(my_list[2])
#     elif my_list[2] == "-":
#         return int(my_list[0]) + int(my_list[1]) - int(my_list[3]) - int(my_list[4])