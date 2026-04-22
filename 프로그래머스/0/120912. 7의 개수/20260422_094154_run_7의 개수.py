def solution(array):
    str_array = ''
    for c in array:
        str_array += c
    
    return str_array

# TypeError: sequence item 0: expected str instance, int found
# def solution(array):
#     answer = "".join(array)
#     return answer