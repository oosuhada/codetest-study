def solution(numbers):
    new_list = []
    for c in numbers:
        new_list.append(abs(c))
    answer = 0
    return new_list