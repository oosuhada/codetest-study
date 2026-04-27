def solution(my_string):
    
    for c in my_string:
        if c.isupper:
            new_string.append(my_string.replace(c,''))
    answer = 0
    return new_string