def solution(array, height):
    new_array = array
    new_array.append(height)
    new_array.sort()
    leng = len(array)
    answer_i = 0
    
    for c in new_array:
        if c == height:
            answer_i = new_array.index(c)
    
    answer = leng - answer_i - 1
    
    return answer

# AttributeError: 'list' object has no attribute 'array'
# def solution(array, height):
#     new_array = array
#     new_array.append(height)
#     new_array2 = new_array.sort(): or new_array2 = new_array.sorted():
    
#     answer = 0
#     return new_array2