def solution(balls, share):
    #경우의 수. balls 중에 share 만큼 고르는 경우의 수
    #answer = balls! / ((balls - share)! * share!)
    
    #balls!
    a = balls
    aa = 1
    while a >= 1:
        aa *= a
        a -= 1 
        
    #share!
    b = share
    bb = 1
    while b >= 1:
        bb *= b
        b -= 1
        
    #(balls - share)!
    c = (balls - share)
    cc = 1
    while c >= 1:
        cc *= c
        c -= 1
        
    return a / (b*c)