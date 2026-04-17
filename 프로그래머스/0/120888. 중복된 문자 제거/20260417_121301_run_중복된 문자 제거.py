def solution(my_string):
    #중복인지를 판별하는게 중요할듯 -> set 사용?
    
    temp_list = list(my_string)
    temp_list2 = list(set(temp_list))
    
    answer = ''
    return temp_list2