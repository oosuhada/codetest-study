def solution(my_string, n):
    answer = ''
    list_string = list(my_string)
    for c in list_string:
        answer += c*n
    return answer