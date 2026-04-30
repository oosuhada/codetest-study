def solution(num_list):
    answer = [a,b]
    a = 0, b = 0
    for c in num_list:
        if c % 2 == 0:
            a += 1
        else:
            b += 1
    return answer