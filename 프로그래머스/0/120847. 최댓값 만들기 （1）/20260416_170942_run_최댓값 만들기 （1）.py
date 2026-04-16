def solution(numbers):
    n = len(numbers)
    arrange(numbers)
    answer = numbers[n] * numbers[n-1]
    return answer