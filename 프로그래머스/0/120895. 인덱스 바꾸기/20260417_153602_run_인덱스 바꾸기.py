def solution(my_string, num1, num2):
    answer = ''
    
    my_list = list(my_string)
    new_list = my_list
    new_list[num1] = my_list[num2]
    new_list[num2] = my_list[num1]
    
    return new_list