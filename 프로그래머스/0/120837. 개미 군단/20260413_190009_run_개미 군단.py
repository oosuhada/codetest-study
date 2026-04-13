def solution(hp):
    #장군개미
    a = hp // 5
    #병정개미
    b = (hp - (hp // 5))//3
    #일개미
    c = hp - (hp // 5) - ((hp - (hp // 5))//3)
    
    return a+b+c