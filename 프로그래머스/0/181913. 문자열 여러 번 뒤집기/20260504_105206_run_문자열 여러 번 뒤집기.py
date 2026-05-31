def solution(my_string, queries):
    answer = my_string
    for row in queries:
        s, e = row
        answer = answer[0:s] + answer[s:e+1][::-1] + answer[e+1:]

    return answer


# answer[s:e][::-1] 뒤집기 방법 힌트 참고함