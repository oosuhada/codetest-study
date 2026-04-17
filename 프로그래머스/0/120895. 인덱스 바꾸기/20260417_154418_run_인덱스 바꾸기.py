def solution(my_string, num1, num2):
    answer = ''
    
    my_list = list(my_string)
    new_list = []
    new_list += my_list
    
    new_list[num1] = my_list[num2]
    
    new_list2 = new_list
    new_list2[num2] = my_list[num1]
    
    return new_list2.join()


# 입력값 〉	"hello", 1, 2
# 기댓값 〉	"hlelo"
# 실행 결과 〉	실행한 결괏값 ["h","l","l","l","o"]이 기댓값 "hlelo"과 다릅니다.
# def solution(my_string, num1, num2):
#     answer = ''
    
#     my_list = list(my_string)
#     new_list = my_list
#     new_list[num1] = my_list[num2]
#     new_list[num2] = my_list[num1]
    
#     return new_list


# def solution(my_string, num1, num2):
#     answer = ''
    
#     my_list = list(my_string)
#     new_list = my_list
    
#     new_list[num1] = my_list[num2]
    
#     new_list2 = new_list
#     new_list2[num2] = my_list[num1]
    
#     return new_list2