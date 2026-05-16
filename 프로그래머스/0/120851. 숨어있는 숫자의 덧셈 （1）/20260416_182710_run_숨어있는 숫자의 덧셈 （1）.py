def solution(my_string):
    
    my_list = []
    #직전 문자열 정렬하기 에서 .isdigit 함수 새로 익히고 활용
    for c in my_string:
        if c.isdigit():
            my_list.append(c)
    
    answer = 0
    for c2 in my_list:
        answer += int(c2)
        
    return answer

