def solution(num_list):
    answer = [0,0]
    for c in num_list:
        if c % 2 == 0:
            answer += [1,0]
        else:
            answer += [0,1]
    return answer