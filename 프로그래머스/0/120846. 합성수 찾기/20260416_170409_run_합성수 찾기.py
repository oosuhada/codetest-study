def solution(n):
    #10 이하 소수 -> 1,2,3,5,7
    #합성수 개수 = n - (n이하 소수 개수)
    #1 < c < n 중 n % c == 0 이 있다면 합성수, 없다면 소수
    #소수를 구하는 함수 고민해봄
    
    verifier = 0
    answer = 0
    x = 2
    # TypeError: 'type' object is not subscriptable
    # range는 함수(정확히는 클래스)라서 소괄호 () 로 호출해야 하는데, 
    # 대괄호 []를 사용했기 때문에 발생한 오류
    while x <= n:
        for c in range(2,x+1):
            if x % c == 0:
                verifier = 1
                x += 1
                if verifier == 1:
                    answer += 1
    
    return answer