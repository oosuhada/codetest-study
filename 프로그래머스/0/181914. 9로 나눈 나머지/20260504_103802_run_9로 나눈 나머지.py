def solution(number):
    sum_number = 0
    for i in number:
        sum_number += int(i)
    return sum_number % 9