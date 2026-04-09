def solution(numbers):
    answer = [null]
    for c in numbers:
        answer += 2*c
    return answer