def solution(array):
    new_array = array.sort()
    m = int(len(new_array)/2)
    answer = new_array[m]
    return answer