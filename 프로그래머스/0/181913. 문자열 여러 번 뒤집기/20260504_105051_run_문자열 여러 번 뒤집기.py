def solution(my_string, queries):
    answer = my_string
    for row in queries:
        s, e = row
        answer = answer[0:s+1] + answer[s:e+1][::-1] + answer[e:]

    return answer