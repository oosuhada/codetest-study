def solution(my_string):
    answer = ''
    for x in my_string:
        if x.isupper:
            answer += x.lower
        else:
            answer += x
    answer = answer.sort()
    return answer