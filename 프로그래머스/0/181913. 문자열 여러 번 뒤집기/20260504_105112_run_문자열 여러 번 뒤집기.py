def solution(my_string, queries):
    answer = my_string
    for row in queries:
        s, e = row
        answer = answer[0:s] + answer[s:e][::-1] + answer[e:]

    return answer