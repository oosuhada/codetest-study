def solution(array, n):
    
    new_array = array
    new_array.append(n)
    new_array.sort()
    
    answer = 0
    return new_array