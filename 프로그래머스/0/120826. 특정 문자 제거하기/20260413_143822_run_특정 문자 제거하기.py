def solution(my_string, letter):
    answer = ''
    if my_string.contains(letter):
        return my_string.delete(letter)
    else:
        return my_string