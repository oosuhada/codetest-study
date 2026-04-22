def solution(array, n):
    answer = 0
    for c in array:
        if c == n:
            answer += 1
    return answer