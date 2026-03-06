def solution(my_string):
    for c in my_string:
        if c.isupper:
            my_string.replace(c,'')
    answer = 0
    return my_string