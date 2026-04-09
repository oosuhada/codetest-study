def solution(array):
    #array 안에 정수 1~9의 개수 구하는법
    
    # for i in range(1,10):
    #     array.count(1)
    
    a = array.count(1)
    b = array.count(2)
    c = array.count(3)
    d = array.count(4)
    e = array.count(5)
    f = array.count(6)
    g = array.count(7)
    h = array.count(8)
    i = array.count(9)

    max(a, b, c, d, e, f, g, h, i)

    answer = 0
    return answer