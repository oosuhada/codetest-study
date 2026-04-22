def solution(array):
    new_array = []
    for c in array:
        new_array.append(str(c))
    str_array = "".join(new_array)
    return str_array.count('7')

# TypeError: sequence item 0: expected str instance, int found
# def solution(array):
#     answer = "".join(array)
#     return answer

# TypeError: can only concatenate str (not "int") to str
# def solution(array):
#     str_array = ''
#     for c in array:
#         str_array += c
#     return str_array