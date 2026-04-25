def solution(array):
    m = len(array.sort())//2
    answer = array.sort()[m]
    return answer