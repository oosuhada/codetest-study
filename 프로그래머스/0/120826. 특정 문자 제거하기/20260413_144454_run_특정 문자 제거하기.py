def solution(my_string, letter):
    answer = ''
    list_my_string = list(my_string)
    if letter in list_my_string:
        return ''.join(list_my_string.remove(str(letter))
    else:
        return my_string
    
#append의 반대 remove 찾아봄
#list to string ''.join 다시 찾아봄

#TypeError: can only join an iterable 오류 발생