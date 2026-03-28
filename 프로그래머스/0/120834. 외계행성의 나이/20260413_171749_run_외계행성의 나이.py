def solution(age):
    # 12를 [1,2] 배열로 바꾸는법 헷갈림. 검색해봄
    # list(map(int, str(age)))
    # int(''.join(map(str, age)))
    
    list1 = list(map(int, str(age)))
    list1.replace(0,a)
    list1.replace(1,b)
    list1.replace(2,c)
    list1.replace(3,d)
    list1.replace(4,e)
    list1.replace(5,f)
    list1.replace(6,g)
    list1.replace(7,h)
    list1.replace(8,i)
    list1.replace(9,j)
    #더 효율적인 한번에 replace 방식 있는지 찾아보기
    return ''.join(list1)
    