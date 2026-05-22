def solution(my_string, letter):
    answer = ''
    list_my_string = list(my_string)
    if letter in list_my_string:
        return ''.(list_my_string.remove(letter))
    else:
        return my_string
    
#append의 반대 remove 찾아봄