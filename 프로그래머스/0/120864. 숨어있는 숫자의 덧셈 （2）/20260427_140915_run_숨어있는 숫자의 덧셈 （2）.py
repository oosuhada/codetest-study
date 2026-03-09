def solution(my_string):
    my_list = []
    for c in my_string:
        if c.isdigit:
            my_list.append(c)
        else:
            my_list.append(my_string.replace(c,''))
            
    answer = 0
    return my_list