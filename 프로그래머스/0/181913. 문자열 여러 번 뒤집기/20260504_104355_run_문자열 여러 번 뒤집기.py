def solution(my_string, queries):
    answer = ''
    for row in queries:
        s, e = row
        my_string = my_string[0:s] + my_string[e:s] + my_string[e:]

    return my_string