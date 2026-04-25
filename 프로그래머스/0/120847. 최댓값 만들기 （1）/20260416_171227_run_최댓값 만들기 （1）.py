def solution(numbers):
    n = len(numbers)
    #작은수부터 큰 수까지 정렬하는 방법 까먹어서 arrage(numbers), array(numbers)
    #numbers.array, numbers.arrange
    #시도하였으나 NameError: name 'array' is not defined
    
    sort(numbers)
    answer = numbers[n] * numbers[n-1]
    return answer