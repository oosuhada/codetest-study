def solution(my_string):
    for c in my_string:
        if c.isupper:
            c.replace('')
    answer = 0
    return my_string