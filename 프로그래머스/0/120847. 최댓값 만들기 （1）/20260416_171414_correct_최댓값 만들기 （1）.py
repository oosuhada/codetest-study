def solution(numbers):
    n = len(numbers)
    #작은수부터 큰 수까지 정렬하는 방법 까먹어서 arrage(numbers), array(numbers)
    #numbers.array, numbers.arrange, sort(numbers)
    #시도하였으나 NameError: name 'array' is not defined 에러
    
    numbers.sort()
    answer = numbers[n-1] * numbers[n-2]
    return answer

    #answer = numbers[n] * numbers[n-1]로 시도해서
    #IndexError: list index out of range 에러 발생