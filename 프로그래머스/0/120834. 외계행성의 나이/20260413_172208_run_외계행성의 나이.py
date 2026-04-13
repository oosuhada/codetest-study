def solution(age):
    # 12를 [1,2] 배열로 바꾸는법 헷갈림. 검색해봄
    # list(map(int, str(age)))
    # int(''.join(map(str, age)))
    
    #list1 = list(map(int, str(age)))
    str1 += str(age)
    #NameError: name 'a' is not defined
    str1.replace('0','a')
    str1.replace('1','b')
    str1.replace('2','c')
    str1.replace('3','d')
    str1.replace('4','e')
    str1.replace('5','f')
    str1.replace('6','g')
    str1.replace('7','h')
    str1.replace('8','i')
    str1.replace('9','j')
    #더 효율적인 한번에 replace 방식 있는지 찾아보기
    return str1
    