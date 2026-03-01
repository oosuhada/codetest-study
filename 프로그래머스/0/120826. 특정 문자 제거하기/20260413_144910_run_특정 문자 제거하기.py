def solution(my_string, letter):
    answer = ''
    list_my_string = list(my_string)
    if letter in list_my_string:
        my_string.replace(letter,"")
        #remove는 하나만 삭제하기 때문에 replace를 써야함
        return my_string
    else:
        return my_string
    
#append의 반대 remove 찾아봄
#list to string ''.join 다시 찾아봄

#TypeError: can only join an iterable 오류 발생