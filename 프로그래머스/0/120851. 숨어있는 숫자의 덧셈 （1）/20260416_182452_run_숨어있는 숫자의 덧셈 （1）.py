def solution(my_string):
    
    new_string = []
    #직전 문자열 정렬하기 에서 .isdigit 함수 새로 익히고 활용
    for c in my_string:
        if c.isdigit():
            new_string.append(c)
            
    answer = 0
    return new_string

