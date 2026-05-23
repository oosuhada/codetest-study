def solution(my_string, queries):
    answer = ''
    for row in queries:
        s, e = row
        answer = my_string[0:s+1] + my_string[e:s+1] + my_string[e:]

    return answer