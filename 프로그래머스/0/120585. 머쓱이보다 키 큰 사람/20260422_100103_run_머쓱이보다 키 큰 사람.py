def solution(array, height):
    new_array = array
    new_array.append(height)
    new_array3 = new_array.sort()
    
    answer = 0
    return new_array