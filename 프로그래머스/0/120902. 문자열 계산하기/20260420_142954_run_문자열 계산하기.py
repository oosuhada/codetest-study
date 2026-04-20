def solution(my_string):
    answer = ','.join(my_string)
    a = answer[0]
    c = answer[4]
    b = answer[8]
    
    if c == +:
        return a + b
    else:
        return a - b