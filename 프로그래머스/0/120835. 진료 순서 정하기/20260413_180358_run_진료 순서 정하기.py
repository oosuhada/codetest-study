def solution(emergency):
    #배열 안에서 큰 숫자부터 1, 2, 3 순서대로 치환하기
    n = len(emergency) #[1부터 n까지 배열]을 숫자 순서대로 치환
    index = list(range(1:n+1))
    #1th, 2nd, 3rd 이런식으로 치환하는 방법이 array 말고 있을까?
    #array(emergency)로 순서를 바꿔버리면 다시 원래대로 돌릴 수 있는 방법이 없지 않나?
    
    while i < n+2:
        for c in emergency:
            max(c).replace('i')
            i += 1 

    return emergency